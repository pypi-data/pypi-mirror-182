import logging
import random
import re
import string
import uuid
from urllib.parse import urlparse, parse_qs
from urllib.request import urlopen

import requests
import yaml

from iacer.exceptions import IacerException
from iacer.plugin.ecs import EcsPlugin
from iacer.plugin.oss import OssPlugin
from iacer.plugin.ros import StackPlugin
from iacer.plugin.vpc import VpcPlugin

LOG = logging.getLogger(__name__)

IAC_OCTOPUS_NAME = 'iacer'


class Selector:

    def __init__(self, key: str, original_value: any,
                 allowed_values: list = None,
                 parameters: dict = None):
        self.key = key
        self.original_value = original_value
        self.allowed_values = allowed_values or []
        self.parameters = parameters
        self.current_value = allowed_values[0] if allowed_values else None
        self.next = None
        self.prev = None

    def refresh_parameters(self):
        self.parameters[self.key] = self.current_value


class LinkedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def append(self, key, original_value, allowed_values=None, parameters=None):
        node = Selector(key, original_value, allowed_values, parameters)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def first(self):
        return self._head

    def __iter__(self):
        cur = self._head
        while cur is not None:
            value = cur.key
            cur = cur.next
            yield value


def _error_message(key, value, msg):
    return f'Parsing pseudo parameter (Key: {key}, Value: {value}) error, {msg}'


class ResolvedParameters:

    def __init__(self, name: str, region: str, parameters: dict):
        self.name = name
        self.region = region
        self.parameters = parameters


class ParamGenerator:
    RE_AUTO = re.compile(fr'\$\[{IAC_OCTOPUS_NAME}-auto]', re.I)
    RE_AUTO_RANDOM = re.compile(fr'\$\[{IAC_OCTOPUS_NAME}-auto[-_]random]', re.I)
    RE_CURRENT_REGION = re.compile(fr'\$\[{IAC_OCTOPUS_NAME}-current[-_]region]', re.I)
    RE_RANDOM_STRING = re.compile(fr'\$\[{IAC_OCTOPUS_NAME}-random[-_]string]', re.I)

    RE_ZONE_ID = re.compile('zone(_|)id', re.I)

    RE_VPC_ID = re.compile('vpc(_|)id', re.I)
    RE_VSW_ID = re.compile('v(_|)switch(_|)id', re.I)
    RE_SECURITY_GROUP = re.compile('security(_|)group(_id|id)', re.I)
    RE_COMMON_NAME = re.compile(r'\w*name', re.I)
    RE_PASSWORD = re.compile(r'\w*password', re.I)
    RE_UUID = re.compile(r'\w*uuid', re.I)

    def __init__(self, config):
        self.config = config
        self.region = config.region
        self.parameters = config.parameters
        self.template_config = config.template_config
        self.parameters_order = config.parameters_order
        self.credential = config.auth.credential
        self.plugin = StackPlugin(region_id=self.region, credential=self.credential)
        self._vpc_id = None
        self._vsw_id = None

    @classmethod
    async def result(cls, config) -> ResolvedParameters:
        pg = cls(config)
        LOG.debug(f'start to generate parameters for {config.test_name}')
        await pg.resolve_auto_random()
        await pg.resolve_auto()
        resolved_parameters = ResolvedParameters(config.test_name, config.region, pg.parameters)
        LOG.debug(f'success generate parameters for {config.test_name}, parameters {resolved_parameters.parameters}')
        return resolved_parameters

    async def resolve_auto(self):
        for key, unresolved_value in self.parameters.items():
            if not isinstance(unresolved_value, str):
                continue
            if self.RE_CURRENT_REGION.match(unresolved_value):
                self.parameters[key] = self.region

            elif self.RE_AUTO.match(unresolved_value):
                if self.RE_VSW_ID.match(key):
                    if self._vsw_id is None:
                        await self._gen_vpc_vsw_id(key, unresolved_value)
                    self.parameters[key] = re.sub(self.RE_AUTO, self._vsw_id, unresolved_value)
                elif self.RE_VPC_ID.match(key):
                    if self._vpc_id is None:
                        await self._gen_vpc_vsw_id(key, unresolved_value)
                    self.parameters[key] = re.sub(self.RE_AUTO, self._vpc_id, unresolved_value)
                elif self.RE_COMMON_NAME.match(key):
                    value = self._gen_common_name()
                    self.parameters[key] = re.sub(self.RE_AUTO, value, unresolved_value)
                elif self.RE_PASSWORD.match(key):
                    value = self._gen_password()
                    self.parameters[key] = re.sub(self.RE_AUTO, value, unresolved_value)
                elif self.RE_UUID.match(key):
                    value = self._gen_uuid()
                    self.parameters[key] = re.sub(self.RE_AUTO, value, unresolved_value)
                elif self.RE_SECURITY_GROUP.match(key):
                    if self._vpc_id is None:
                        self._vpc_id, self._vsw_id = await self._gen_vpc_vsw_id(key, unresolved_value)
                    value = await self._gen_sg(key, unresolved_value)
                    self.parameters[key] = re.sub(self.RE_AUTO, value, unresolved_value)

        return self.parameters

    async def resolve_auto_random(self):
        linked_list = LinkedList()
        resolved_parameters = {}
        unresolved_parameters = {}
        parameters_order = self.parameters_order
        if not parameters_order:
            parameters_order = await self._get_parameters_order() or self.parameters.keys()
        for key in parameters_order:
            if key not in self.parameters:
                continue
            original_value = self.parameters[key]
            if isinstance(original_value, str) and self.RE_AUTO_RANDOM.match(original_value):
                resolved_parameters[key] = None
                linked_list.append(key, original_value, parameters=resolved_parameters)
            elif self.RE_ZONE_ID.match(key) and (
                self.RE_AUTO.match(original_value) or self.RE_AUTO_RANDOM.match(original_value)
            ):
                resolved_parameters[key] = None
                linked_list.append(key, original_value, parameters=resolved_parameters)
            elif isinstance(original_value, str) and self.RE_AUTO.match(original_value):
                unresolved_parameters[key] = original_value
                resolved_parameters[key] = None
            else:
                resolved_parameters[key] = original_value

        first_selector = linked_list.first()
        if not first_selector:
            return resolved_parameters
        resolved_parameters = await self._select_value(first_selector)
        resolved_parameters.update(unresolved_parameters)
        self.parameters.update(resolved_parameters)
        return self.parameters

    async def _select_value(self, selector: Selector) -> dict:
        key = selector.key
        parameters = selector.parameters
        allowed_values = selector.allowed_values
        current_value = selector.current_value
        error_msg = f'can not find any available value for {key} in {self.region} region ' \
                    f'in {allowed_values} for {self.config.test_name}'

        if allowed_values:
            next_selector = selector.next
            if not next_selector:
                return selector.parameters
            index = allowed_values.index(current_value)
            if index + 1 >= len(allowed_values):
                prev_selector = selector.prev
                if not prev_selector:
                    raise IacerException(error_msg)
                return await self._select_value(prev_selector)
            selector.current_value = allowed_values[index + 1]
            next_selector.parameters[key] = selector.current_value
            next_selector.allowed_values = []
            return await self._select_value(next_selector)

        constraints = await self.plugin.get_parameter_constraints(
            parameters=parameters,
            **self.template_config.to_dict(),
            parameters_key_filter=[key]
        )
        values = constraints[0].get('AllowedValues') if constraints else []
        if not values:
            prev_selector = selector.prev
            if not prev_selector:
                raise IacerException(error_msg)
            return await self._select_value(prev_selector)

        selector.allowed_values = values
        selector.current_value = values[0]
        selector.parameters[key] = selector.current_value
        next_selector = selector.next
        if not next_selector:
            return selector.parameters
        next_selector.parameters[key] = selector.current_value
        return await self._select_value(next_selector)

    async def _get_parameters_order(self):
        template = await self._get_template_body()
        if not template:
            raise IacerException(f'failed to retrieve template by template config {self.template_config}')
        parsed_tpl = yaml.safe_load(template)
        param_groups = parsed_tpl.get('Metadata', {}).get('ALIYUN::ROS::Interface', {}).get('ParameterGroups', [])
        if not param_groups:
            return
        params_in_metadata = []
        for param_group in param_groups:
            params = param_group.get('Parameters', []) if param_group else None
            if not params:
                continue
            standard_params = [p for p in params if isinstance(p, str)]
            params_in_metadata += standard_params

        return params_in_metadata

    template_max_size = 524288

    async def _get_template_body(self):
        template_body = self.template_config.template_body
        if template_body:
            return template_body

        template_id = self.template_config.template_id
        if template_id:
            try:
                template_info = await self.plugin.get_template(
                    template_id=template_id,
                    template_version=self.template_config.template_version
                )
                return template_info['TemplateBody']
            except Exception as ex:
                raise IacerException(f'Failed to retrieve {template_id}: {ex}')

        template_url = self.template_config.template_url
        if template_url:
            components = urlparse(template_url)
            if components.scheme == 'oss':
                return self._get_template_from_oss(template_url, components)
            elif components.scheme == 'file':
                try:
                    return urlopen(template_url).read()
                except Exception as ex:
                    raise IacerException(f'Failed to retrieve {template_url}: {ex}')
            else:
                try:
                    resp = requests.get(template_url, timeout=10, stream=True)
                    resp.raise_for_status()

                    reader = resp.iter_content(chunk_size=1000)
                    result = b''
                    max_size = self.template_max_size
                    for chunk in reader:
                        result += chunk
                        if len(result) > max_size:
                            raise IacerException(f'template from {template_url}'
                                                 f'exceeds maximum allowed size ({max_size} bytes)')
                    return result
                except Exception as ex:
                    raise IacerException(f'Failed to retrieve {template_url}: {ex}')

    def _get_template_from_oss(self, template_url, components):
        bucket_name = components.netloc
        object_path = components.path.strip('/')
        if not bucket_name or not object_path:
            raise IacerException(f'Invalid oss url {template_url}')
        region_id = self.region
        if components.query:
            t = parse_qs(components.query)
            region_ids = t.get('RegionId')
            region_id = region_ids[0] if region_ids else self.region

        oss_plugin = OssPlugin(region_id=region_id, bucket_name=bucket_name, credential=self.credential)
        try:
            object_meta = oss_plugin.get_object_meta(object_path)
        except Exception as ex:
            raise IacerException(f'Oss failed: {ex}')
        if object_meta is None:
            raise IacerException(f'Invalid oss url {template_url}')
        if object_meta.content_length > self.template_max_size:
            raise IacerException(f'template from {template_url} exceeds maximum allowed size (524288 bytes)')

        try:
            r = oss_plugin.get_object_content(object_path)
        except Exception as ex:
            raise IacerException(f'Oss failed: {ex}')
        if r is None:
            raise IacerException(f'Invalid oss url {template_url}')
        return r.read()

    async def _gen_vpc_id(self, key, value):
        plugin = VpcPlugin(self.region, credential=self.credential)
        vpc = await plugin.get_one_vpc()
        if not vpc:
            msg = f'can not find any vpc in region {self.region}'
            raise IacerException(_error_message(key, value, msg))
        return vpc['VpcId']

    async def _gen_vpc_vsw_id(self, key, value):
        zone_id = None
        for name, value in self.parameters.items():
            if self.RE_ZONE_ID.match(name):
                zone_id = value
                break

        plugin = VpcPlugin(self.region, credential=self.credential)
        vsw = await plugin.get_one_vswitch(zone_id=zone_id)
        if not vsw:
            msg = f'can not find any vswitch in zone {zone_id}'
            raise IacerException(_error_message(key, value, msg))
        self._vpc_id = vsw['VpcId']
        self._vsw_id = vsw['VSwitchId']
        return self._vpc_id, self._vsw_id

    def _gen_common_name(self):
        return f'{IAC_OCTOPUS_NAME}-{uuid.uuid1().hex}'[:50]

    def _gen_password(self):
        special_chars = '!#$&{*:[=,]-_%@+'
        password_chars = []
        for item in (string.ascii_lowercase, special_chars, string.digits, string.ascii_uppercase):
            password_chars.extend(random.sample(item, 4))
        return ''.join(password_chars)

    def _gen_uuid(self):
        return str(uuid.uuid1())

    async def _gen_sg(self, key, value):
        if self._vpc_id is None:
            await self._gen_vpc_vsw_id(key, value)
        plugin = EcsPlugin(region_id=self.region, credential=self.credential)
        sg = await plugin.get_security_group(vpc_id=self._vpc_id)
        if not sg:
            msg = f'can not find security group in vpc {self._vpc_id} in {self.region} region'
            raise IacerException(_error_message(key, value, msg))
        return sg['SecurityGroupId']

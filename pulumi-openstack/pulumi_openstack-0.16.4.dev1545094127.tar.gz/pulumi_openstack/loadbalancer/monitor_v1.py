# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class MonitorV1(pulumi.CustomResource):
    """
    Manages a V1 load balancer monitor resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, admin_state_up=None, delay=None, expected_codes=None, http_method=None, max_retries=None, region=None, tenant_id=None, timeout=None, type=None, url_path=None):
        """Create a MonitorV1 resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['admin_state_up'] = admin_state_up

        if not delay:
            raise TypeError('Missing required property delay')
        __props__['delay'] = delay

        __props__['expected_codes'] = expected_codes

        __props__['http_method'] = http_method

        if not max_retries:
            raise TypeError('Missing required property max_retries')
        __props__['max_retries'] = max_retries

        __props__['region'] = region

        __props__['tenant_id'] = tenant_id

        if not timeout:
            raise TypeError('Missing required property timeout')
        __props__['timeout'] = timeout

        if not type:
            raise TypeError('Missing required property type')
        __props__['type'] = type

        __props__['url_path'] = url_path

        super(MonitorV1, __self__).__init__(
            'openstack:loadbalancer/monitorV1:MonitorV1',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


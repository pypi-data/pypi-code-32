# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Network(pulumi.CustomResource):
    """
    Manages a V2 Neutron network resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, admin_state_up=None, availability_zone_hints=None, external=None, name=None, region=None, segments=None, shared=None, tags=None, tenant_id=None, value_specs=None):
        """Create a Network resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['admin_state_up'] = admin_state_up

        __props__['availability_zone_hints'] = availability_zone_hints

        __props__['external'] = external

        __props__['name'] = name

        __props__['region'] = region

        __props__['segments'] = segments

        __props__['shared'] = shared

        __props__['tags'] = tags

        __props__['tenant_id'] = tenant_id

        __props__['value_specs'] = value_specs

        super(Network, __self__).__init__(
            'openstack:networking/network:Network',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


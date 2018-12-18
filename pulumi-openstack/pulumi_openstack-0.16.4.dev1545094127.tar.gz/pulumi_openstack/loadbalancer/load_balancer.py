# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class LoadBalancer(pulumi.CustomResource):
    """
    Manages a V2 loadbalancer resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, admin_state_up=None, description=None, flavor=None, loadbalancer_provider=None, name=None, region=None, security_group_ids=None, tenant_id=None, vip_address=None, vip_subnet_id=None):
        """Create a LoadBalancer resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['admin_state_up'] = admin_state_up

        __props__['description'] = description

        __props__['flavor'] = flavor

        __props__['loadbalancer_provider'] = loadbalancer_provider

        __props__['name'] = name

        __props__['region'] = region

        __props__['security_group_ids'] = security_group_ids

        __props__['tenant_id'] = tenant_id

        __props__['vip_address'] = vip_address

        if not vip_subnet_id:
            raise TypeError('Missing required property vip_subnet_id')
        __props__['vip_subnet_id'] = vip_subnet_id

        __props__['vip_port_id'] = None

        super(LoadBalancer, __self__).__init__(
            'openstack:loadbalancer/loadBalancer:LoadBalancer',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


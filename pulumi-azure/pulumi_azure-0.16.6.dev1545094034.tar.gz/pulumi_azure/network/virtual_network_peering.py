# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class VirtualNetworkPeering(pulumi.CustomResource):
    """
    Manages a virtual network peering which allows resources to access other
    resources in the linked virtual network.
    """
    def __init__(__self__, __name__, __opts__=None, allow_forwarded_traffic=None, allow_gateway_transit=None, allow_virtual_network_access=None, name=None, remote_virtual_network_id=None, resource_group_name=None, use_remote_gateways=None, virtual_network_name=None):
        """Create a VirtualNetworkPeering resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['allow_forwarded_traffic'] = allow_forwarded_traffic

        __props__['allow_gateway_transit'] = allow_gateway_transit

        __props__['allow_virtual_network_access'] = allow_virtual_network_access

        __props__['name'] = name

        if not remote_virtual_network_id:
            raise TypeError('Missing required property remote_virtual_network_id')
        __props__['remote_virtual_network_id'] = remote_virtual_network_id

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['use_remote_gateways'] = use_remote_gateways

        if not virtual_network_name:
            raise TypeError('Missing required property virtual_network_name')
        __props__['virtual_network_name'] = virtual_network_name

        super(VirtualNetworkPeering, __self__).__init__(
            'azure:network/virtualNetworkPeering:VirtualNetworkPeering',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


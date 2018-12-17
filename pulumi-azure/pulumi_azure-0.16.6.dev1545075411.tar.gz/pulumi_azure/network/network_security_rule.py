# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class NetworkSecurityRule(pulumi.CustomResource):
    """
    Manages a Network Security Rule.
    
    ~> **NOTE on Network Security Groups and Network Security Rules:** Terraform currently
    provides both a standalone Network Security Rule resource, and allows for Network Security Rules to be defined in-line within the Network Security Group resource.
    At this time you cannot use a Network Security Group with in-line Network Security Rules in conjunction with any Network Security Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules.
    """
    def __init__(__self__, __name__, __opts__=None, access=None, description=None, destination_address_prefix=None, destination_address_prefixes=None, destination_application_security_group_ids=None, destination_port_range=None, destination_port_ranges=None, direction=None, name=None, network_security_group_name=None, priority=None, protocol=None, resource_group_name=None, source_address_prefix=None, source_address_prefixes=None, source_application_security_group_ids=None, source_port_range=None, source_port_ranges=None):
        """Create a NetworkSecurityRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not access:
            raise TypeError('Missing required property access')
        __props__['access'] = access

        __props__['description'] = description

        __props__['destination_address_prefix'] = destination_address_prefix

        __props__['destination_address_prefixes'] = destination_address_prefixes

        __props__['destination_application_security_group_ids'] = destination_application_security_group_ids

        __props__['destination_port_range'] = destination_port_range

        __props__['destination_port_ranges'] = destination_port_ranges

        if not direction:
            raise TypeError('Missing required property direction')
        __props__['direction'] = direction

        __props__['name'] = name

        if not network_security_group_name:
            raise TypeError('Missing required property network_security_group_name')
        __props__['network_security_group_name'] = network_security_group_name

        if not priority:
            raise TypeError('Missing required property priority')
        __props__['priority'] = priority

        if not protocol:
            raise TypeError('Missing required property protocol')
        __props__['protocol'] = protocol

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['source_address_prefix'] = source_address_prefix

        __props__['source_address_prefixes'] = source_address_prefixes

        __props__['source_application_security_group_ids'] = source_application_security_group_ids

        __props__['source_port_range'] = source_port_range

        __props__['source_port_ranges'] = source_port_ranges

        super(NetworkSecurityRule, __self__).__init__(
            'azure:network/networkSecurityRule:NetworkSecurityRule',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


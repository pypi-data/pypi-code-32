# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class ARecord(pulumi.CustomResource):
    """
    Enables you to manage DNS A Records within Azure DNS.
    """
    def __init__(__self__, __name__, __opts__=None, name=None, records=None, resource_group_name=None, tags=None, ttl=None, zone_name=None):
        """Create a ARecord resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['name'] = name

        if not records:
            raise TypeError('Missing required property records')
        __props__['records'] = records

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['tags'] = tags

        if not ttl:
            raise TypeError('Missing required property ttl')
        __props__['ttl'] = ttl

        if not zone_name:
            raise TypeError('Missing required property zone_name')
        __props__['zone_name'] = zone_name

        super(ARecord, __self__).__init__(
            'azure:dns/aRecord:ARecord',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


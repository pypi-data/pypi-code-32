# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Endpoint(pulumi.CustomResource):
    """
    A CDN Endpoint is the entity within a CDN Profile containing configuration information regarding caching behaviors and origins. The CDN Endpoint is exposed using the URL format <endpointname>.azureedge.net.
    """
    def __init__(__self__, __name__, __opts__=None, content_types_to_compresses=None, geo_filters=None, is_compression_enabled=None, is_http_allowed=None, is_https_allowed=None, location=None, name=None, optimization_type=None, origins=None, origin_host_header=None, origin_path=None, probe_path=None, profile_name=None, querystring_caching_behaviour=None, resource_group_name=None, tags=None):
        """Create a Endpoint resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['content_types_to_compresses'] = content_types_to_compresses

        __props__['geo_filters'] = geo_filters

        __props__['is_compression_enabled'] = is_compression_enabled

        __props__['is_http_allowed'] = is_http_allowed

        __props__['is_https_allowed'] = is_https_allowed

        if not location:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['name'] = name

        __props__['optimization_type'] = optimization_type

        if not origins:
            raise TypeError('Missing required property origins')
        __props__['origins'] = origins

        __props__['origin_host_header'] = origin_host_header

        __props__['origin_path'] = origin_path

        __props__['probe_path'] = probe_path

        if not profile_name:
            raise TypeError('Missing required property profile_name')
        __props__['profile_name'] = profile_name

        __props__['querystring_caching_behaviour'] = querystring_caching_behaviour

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['tags'] = tags

        __props__['host_name'] = None

        super(Endpoint, __self__).__init__(
            'azure:cdn/endpoint:Endpoint',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


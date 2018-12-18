# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class RouterInterface(pulumi.CustomResource):
    """
    Manages a Cloud Router interface. For more information see
    [the official documentation](https://cloud.google.com/compute/docs/cloudrouter)
    and
    [API](https://cloud.google.com/compute/docs/reference/latest/routers).
    """
    def __init__(__self__, __name__, __opts__=None, ip_range=None, name=None, project=None, region=None, router=None, vpn_tunnel=None):
        """Create a RouterInterface resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['ip_range'] = ip_range

        __props__['name'] = name

        __props__['project'] = project

        __props__['region'] = region

        if not router:
            raise TypeError('Missing required property router')
        __props__['router'] = router

        if not vpn_tunnel:
            raise TypeError('Missing required property vpn_tunnel')
        __props__['vpn_tunnel'] = vpn_tunnel

        super(RouterInterface, __self__).__init__(
            'gcp:compute/routerInterface:RouterInterface',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


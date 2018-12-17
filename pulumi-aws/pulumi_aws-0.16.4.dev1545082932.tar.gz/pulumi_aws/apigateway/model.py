# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Model(pulumi.CustomResource):
    """
    Provides a Model for a API Gateway.
    """
    def __init__(__self__, __name__, __opts__=None, content_type=None, description=None, name=None, rest_api=None, schema=None):
        """Create a Model resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not content_type:
            raise TypeError('Missing required property content_type')
        __props__['content_type'] = content_type

        __props__['description'] = description

        __props__['name'] = name

        if not rest_api:
            raise TypeError('Missing required property rest_api')
        __props__['rest_api'] = rest_api

        __props__['schema'] = schema

        super(Model, __self__).__init__(
            'aws:apigateway/model:Model',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


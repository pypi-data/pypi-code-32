# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Service(pulumi.CustomResource):
    """
    This resource creates and rolls out a Cloud Endpoints service using OpenAPI or gRPC.  View the relevant docs for [OpenAPI](https://cloud.google.com/endpoints/docs/openapi/) and [gRPC](https://cloud.google.com/endpoints/docs/grpc/).
    """
    def __init__(__self__, __name__, __opts__=None, grpc_config=None, openapi_config=None, project=None, protoc_output=None, protoc_output_base64=None, service_name=None):
        """Create a Service resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['grpc_config'] = grpc_config

        __props__['openapi_config'] = openapi_config

        __props__['project'] = project

        __props__['protoc_output'] = protoc_output

        __props__['protoc_output_base64'] = protoc_output_base64

        if not service_name:
            raise TypeError('Missing required property service_name')
        __props__['service_name'] = service_name

        __props__['apis'] = None
        __props__['config_id'] = None
        __props__['dns_address'] = None
        __props__['endpoints'] = None

        super(Service, __self__).__init__(
            'gcp:endpoints/service:Service',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


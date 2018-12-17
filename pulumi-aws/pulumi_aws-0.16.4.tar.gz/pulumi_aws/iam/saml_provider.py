# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class SamlProvider(pulumi.CustomResource):
    """
    Provides an IAM SAML provider.
    """
    def __init__(__self__, __name__, __opts__=None, name=None, saml_metadata_document=None):
        """Create a SamlProvider resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['name'] = name

        if not saml_metadata_document:
            raise TypeError('Missing required property saml_metadata_document')
        __props__['saml_metadata_document'] = saml_metadata_document

        __props__['arn'] = None
        __props__['valid_until'] = None

        super(SamlProvider, __self__).__init__(
            'aws:iam/samlProvider:SamlProvider',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


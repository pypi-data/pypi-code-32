# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class LogResourcePolicy(pulumi.CustomResource):
    """
    Provides a resource to manage a CloudWatch log resource policy.
    """
    def __init__(__self__, __name__, __opts__=None, policy_document=None, policy_name=None):
        """Create a LogResourcePolicy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not policy_document:
            raise TypeError('Missing required property policy_document')
        __props__['policy_document'] = policy_document

        if not policy_name:
            raise TypeError('Missing required property policy_name')
        __props__['policy_name'] = policy_name

        super(LogResourcePolicy, __self__).__init__(
            'aws:cloudwatch/logResourcePolicy:LogResourcePolicy',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


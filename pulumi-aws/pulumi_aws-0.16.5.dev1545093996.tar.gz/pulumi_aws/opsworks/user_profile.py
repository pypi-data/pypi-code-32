# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class UserProfile(pulumi.CustomResource):
    """
    Provides an OpsWorks User Profile resource.
    """
    def __init__(__self__, __name__, __opts__=None, allow_self_management=None, ssh_public_key=None, ssh_username=None, user_arn=None):
        """Create a UserProfile resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['allow_self_management'] = allow_self_management

        __props__['ssh_public_key'] = ssh_public_key

        if not ssh_username:
            raise TypeError('Missing required property ssh_username')
        __props__['ssh_username'] = ssh_username

        if not user_arn:
            raise TypeError('Missing required property user_arn')
        __props__['user_arn'] = user_arn

        super(UserProfile, __self__).__init__(
            'aws:opsworks/userProfile:UserProfile',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


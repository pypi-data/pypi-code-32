# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class IdentityPoolRoleAttachment(pulumi.CustomResource):
    """
    Provides an AWS Cognito Identity Pool Roles Attachment.
    """
    def __init__(__self__, __name__, __opts__=None, identity_pool_id=None, role_mappings=None, roles=None):
        """Create a IdentityPoolRoleAttachment resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not identity_pool_id:
            raise TypeError('Missing required property identity_pool_id')
        __props__['identity_pool_id'] = identity_pool_id

        __props__['role_mappings'] = role_mappings

        if not roles:
            raise TypeError('Missing required property roles')
        __props__['roles'] = roles

        super(IdentityPoolRoleAttachment, __self__).__init__(
            'aws:cognito/identityPoolRoleAttachment:IdentityPoolRoleAttachment',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


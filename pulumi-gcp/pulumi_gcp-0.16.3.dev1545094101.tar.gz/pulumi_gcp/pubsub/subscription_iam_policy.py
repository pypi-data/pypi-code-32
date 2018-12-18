# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class SubscriptionIAMPolicy(pulumi.CustomResource):
    """
    Three different resources help you manage your IAM policy for pubsub subscription. Each of these resources serves a different use case:
    
    * `google_pubsub_subscription_iam_policy`: Authoritative. Sets the IAM policy for the subscription and replaces any existing policy already attached.
    * `google_pubsub_subscription_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the subscription are preserved.
    * `google_pubsub_subscription_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the subscription are preserved.
    
    ~> **Note:** `google_pubsub_subscription_iam_policy` **cannot** be used in conjunction with `google_pubsub_subscription_iam_binding` and `google_pubsub_subscription_iam_member` or they will fight over what your policy should be.
    
    ~> **Note:** `google_pubsub_subscription_iam_binding` resources **can be** used in conjunction with `google_pubsub_subscription_iam_member` resources **only if** they do not grant privilege to the same role.
    """
    def __init__(__self__, __name__, __opts__=None, policy_data=None, project=None, subscription=None):
        """Create a SubscriptionIAMPolicy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not policy_data:
            raise TypeError('Missing required property policy_data')
        __props__['policy_data'] = policy_data

        __props__['project'] = project

        if not subscription:
            raise TypeError('Missing required property subscription')
        __props__['subscription'] = subscription

        __props__['etag'] = None

        super(SubscriptionIAMPolicy, __self__).__init__(
            'gcp:pubsub/subscriptionIAMPolicy:SubscriptionIAMPolicy',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class JobQueue(pulumi.CustomResource):
    """
    Provides a Batch Job Queue resource.
    """
    def __init__(__self__, __name__, __opts__=None, compute_environments=None, name=None, priority=None, state=None):
        """Create a JobQueue resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not compute_environments:
            raise TypeError('Missing required property compute_environments')
        __props__['compute_environments'] = compute_environments

        __props__['name'] = name

        if not priority:
            raise TypeError('Missing required property priority')
        __props__['priority'] = priority

        if not state:
            raise TypeError('Missing required property state')
        __props__['state'] = state

        __props__['arn'] = None

        super(JobQueue, __self__).__init__(
            'aws:batch/jobQueue:JobQueue',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


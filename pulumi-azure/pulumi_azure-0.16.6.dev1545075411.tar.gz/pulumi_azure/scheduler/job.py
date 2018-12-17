# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Job(pulumi.CustomResource):
    """
    Manages a Scheduler Job.
    
    ~> **NOTE:** Support for Scheduler Job has been deprecated by Microsoft in favour of Logic Apps ([more information can be found at this link](https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps)) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.
    """
    def __init__(__self__, __name__, __opts__=None, action_storage_queue=None, action_web=None, error_action_storage_queue=None, error_action_web=None, job_collection_name=None, name=None, recurrence=None, resource_group_name=None, retry=None, start_time=None, state=None):
        """Create a Job resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['action_storage_queue'] = action_storage_queue

        __props__['action_web'] = action_web

        __props__['error_action_storage_queue'] = error_action_storage_queue

        __props__['error_action_web'] = error_action_web

        if not job_collection_name:
            raise TypeError('Missing required property job_collection_name')
        __props__['job_collection_name'] = job_collection_name

        __props__['name'] = name

        __props__['recurrence'] = recurrence

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['retry'] = retry

        __props__['start_time'] = start_time

        __props__['state'] = state

        super(Job, __self__).__init__(
            'azure:scheduler/job:Job',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


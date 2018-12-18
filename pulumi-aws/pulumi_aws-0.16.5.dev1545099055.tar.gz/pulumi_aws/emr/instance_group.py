# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class InstanceGroup(pulumi.CustomResource):
    """
    Provides an Elastic MapReduce Cluster Instance Group configuration.
    See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/emr/) for more information.
    
    ~> **NOTE:** At this time, Instance Groups cannot be destroyed through the API nor
    web interface. Instance Groups are destroyed when the EMR Cluster is destroyed.
    Terraform will resize any Instance Group to zero when destroying the resource.
    """
    def __init__(__self__, __name__, __opts__=None, cluster_id=None, ebs_configs=None, ebs_optimized=None, instance_count=None, instance_type=None, name=None):
        """Create a InstanceGroup resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not cluster_id:
            raise TypeError('Missing required property cluster_id')
        __props__['cluster_id'] = cluster_id

        __props__['ebs_configs'] = ebs_configs

        __props__['ebs_optimized'] = ebs_optimized

        __props__['instance_count'] = instance_count

        if not instance_type:
            raise TypeError('Missing required property instance_type')
        __props__['instance_type'] = instance_type

        __props__['name'] = name

        __props__['running_instance_count'] = None
        __props__['status'] = None

        super(InstanceGroup, __self__).__init__(
            'aws:emr/instanceGroup:InstanceGroup',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


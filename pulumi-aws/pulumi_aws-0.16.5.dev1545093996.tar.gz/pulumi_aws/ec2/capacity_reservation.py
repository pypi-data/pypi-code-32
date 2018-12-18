# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class CapacityReservation(pulumi.CustomResource):
    """
    Provides an EC2 Capacity Reservation. This allows you to reserve capacity for your Amazon EC2 instances in a specific Availability Zone for any duration.
    """
    def __init__(__self__, __name__, __opts__=None, availability_zone=None, ebs_optimized=None, end_date=None, end_date_type=None, ephemeral_storage=None, instance_count=None, instance_match_criteria=None, instance_platform=None, instance_type=None, tags=None, tenancy=None):
        """Create a CapacityReservation resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not availability_zone:
            raise TypeError('Missing required property availability_zone')
        __props__['availability_zone'] = availability_zone

        __props__['ebs_optimized'] = ebs_optimized

        __props__['end_date'] = end_date

        __props__['end_date_type'] = end_date_type

        __props__['ephemeral_storage'] = ephemeral_storage

        if not instance_count:
            raise TypeError('Missing required property instance_count')
        __props__['instance_count'] = instance_count

        __props__['instance_match_criteria'] = instance_match_criteria

        if not instance_platform:
            raise TypeError('Missing required property instance_platform')
        __props__['instance_platform'] = instance_platform

        if not instance_type:
            raise TypeError('Missing required property instance_type')
        __props__['instance_type'] = instance_type

        __props__['tags'] = tags

        __props__['tenancy'] = tenancy

        super(CapacityReservation, __self__).__init__(
            'aws:ec2/capacityReservation:CapacityReservation',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


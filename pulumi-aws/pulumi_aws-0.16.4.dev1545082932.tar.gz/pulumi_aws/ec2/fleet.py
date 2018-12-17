# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Fleet(pulumi.CustomResource):
    """
    Provides a resource to manage EC2 Fleets.
    """
    def __init__(__self__, __name__, __opts__=None, excess_capacity_termination_policy=None, launch_template_config=None, on_demand_options=None, replace_unhealthy_instances=None, spot_options=None, tags=None, target_capacity_specification=None, terminate_instances=None, terminate_instances_with_expiration=None, type=None):
        """Create a Fleet resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['excess_capacity_termination_policy'] = excess_capacity_termination_policy

        if not launch_template_config:
            raise TypeError('Missing required property launch_template_config')
        __props__['launch_template_config'] = launch_template_config

        __props__['on_demand_options'] = on_demand_options

        __props__['replace_unhealthy_instances'] = replace_unhealthy_instances

        __props__['spot_options'] = spot_options

        __props__['tags'] = tags

        if not target_capacity_specification:
            raise TypeError('Missing required property target_capacity_specification')
        __props__['target_capacity_specification'] = target_capacity_specification

        __props__['terminate_instances'] = terminate_instances

        __props__['terminate_instances_with_expiration'] = terminate_instances_with_expiration

        __props__['type'] = type

        super(Fleet, __self__).__init__(
            'aws:ec2/fleet:Fleet',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


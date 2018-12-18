# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Cluster(pulumi.CustomResource):
    """
    Provides a DAX Cluster resource.
    """
    def __init__(__self__, __name__, __opts__=None, availability_zones=None, cluster_name=None, description=None, iam_role_arn=None, maintenance_window=None, node_type=None, notification_topic_arn=None, parameter_group_name=None, replication_factor=None, security_group_ids=None, server_side_encryption=None, subnet_group_name=None, tags=None):
        """Create a Cluster resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['availability_zones'] = availability_zones

        if not cluster_name:
            raise TypeError('Missing required property cluster_name')
        __props__['cluster_name'] = cluster_name

        __props__['description'] = description

        if not iam_role_arn:
            raise TypeError('Missing required property iam_role_arn')
        __props__['iam_role_arn'] = iam_role_arn

        __props__['maintenance_window'] = maintenance_window

        if not node_type:
            raise TypeError('Missing required property node_type')
        __props__['node_type'] = node_type

        __props__['notification_topic_arn'] = notification_topic_arn

        __props__['parameter_group_name'] = parameter_group_name

        if not replication_factor:
            raise TypeError('Missing required property replication_factor')
        __props__['replication_factor'] = replication_factor

        __props__['security_group_ids'] = security_group_ids

        __props__['server_side_encryption'] = server_side_encryption

        __props__['subnet_group_name'] = subnet_group_name

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['cluster_address'] = None
        __props__['configuration_endpoint'] = None
        __props__['nodes'] = None
        __props__['port'] = None

        super(Cluster, __self__).__init__(
            'aws:dax/cluster:Cluster',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Cluster(pulumi.CustomResource):
    """
    Provides a Redshift Cluster Resource.
    
    ~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    """
    def __init__(__self__, __name__, __opts__=None, allow_version_upgrade=None, automated_snapshot_retention_period=None, availability_zone=None, bucket_name=None, cluster_identifier=None, cluster_parameter_group_name=None, cluster_public_key=None, cluster_revision_number=None, cluster_security_groups=None, cluster_subnet_group_name=None, cluster_type=None, cluster_version=None, database_name=None, elastic_ip=None, enable_logging=None, encrypted=None, endpoint=None, enhanced_vpc_routing=None, final_snapshot_identifier=None, iam_roles=None, kms_key_id=None, logging=None, master_password=None, master_username=None, node_type=None, number_of_nodes=None, owner_account=None, port=None, preferred_maintenance_window=None, publicly_accessible=None, s3_key_prefix=None, skip_final_snapshot=None, snapshot_cluster_identifier=None, snapshot_copy=None, snapshot_identifier=None, tags=None, vpc_security_group_ids=None):
        """Create a Cluster resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['allow_version_upgrade'] = allow_version_upgrade

        __props__['automated_snapshot_retention_period'] = automated_snapshot_retention_period

        __props__['availability_zone'] = availability_zone

        __props__['bucket_name'] = bucket_name

        if not cluster_identifier:
            raise TypeError('Missing required property cluster_identifier')
        __props__['cluster_identifier'] = cluster_identifier

        __props__['cluster_parameter_group_name'] = cluster_parameter_group_name

        __props__['cluster_public_key'] = cluster_public_key

        __props__['cluster_revision_number'] = cluster_revision_number

        __props__['cluster_security_groups'] = cluster_security_groups

        __props__['cluster_subnet_group_name'] = cluster_subnet_group_name

        __props__['cluster_type'] = cluster_type

        __props__['cluster_version'] = cluster_version

        __props__['database_name'] = database_name

        __props__['elastic_ip'] = elastic_ip

        __props__['enable_logging'] = enable_logging

        __props__['encrypted'] = encrypted

        __props__['endpoint'] = endpoint

        __props__['enhanced_vpc_routing'] = enhanced_vpc_routing

        __props__['final_snapshot_identifier'] = final_snapshot_identifier

        __props__['iam_roles'] = iam_roles

        __props__['kms_key_id'] = kms_key_id

        __props__['logging'] = logging

        __props__['master_password'] = master_password

        __props__['master_username'] = master_username

        if not node_type:
            raise TypeError('Missing required property node_type')
        __props__['node_type'] = node_type

        __props__['number_of_nodes'] = number_of_nodes

        __props__['owner_account'] = owner_account

        __props__['port'] = port

        __props__['preferred_maintenance_window'] = preferred_maintenance_window

        __props__['publicly_accessible'] = publicly_accessible

        __props__['s3_key_prefix'] = s3_key_prefix

        __props__['skip_final_snapshot'] = skip_final_snapshot

        __props__['snapshot_cluster_identifier'] = snapshot_cluster_identifier

        __props__['snapshot_copy'] = snapshot_copy

        __props__['snapshot_identifier'] = snapshot_identifier

        __props__['tags'] = tags

        __props__['vpc_security_group_ids'] = vpc_security_group_ids

        __props__['dns_name'] = None

        super(Cluster, __self__).__init__(
            'aws:redshift/cluster:Cluster',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Bucket(pulumi.CustomResource):
    """
    Provides a S3 bucket resource.
    """
    def __init__(__self__, __name__, __opts__=None, acceleration_status=None, acl=None, arn=None, bucket=None, bucket_prefix=None, cors_rules=None, force_destroy=None, hosted_zone_id=None, lifecycle_rules=None, loggings=None, policy=None, region=None, replication_configuration=None, request_payer=None, server_side_encryption_configuration=None, tags=None, versioning=None, website=None, website_domain=None, website_endpoint=None):
        """Create a Bucket resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['acceleration_status'] = acceleration_status

        __props__['acl'] = acl

        __props__['arn'] = arn

        __props__['bucket'] = bucket

        __props__['bucket_prefix'] = bucket_prefix

        __props__['cors_rules'] = cors_rules

        __props__['force_destroy'] = force_destroy

        __props__['hosted_zone_id'] = hosted_zone_id

        __props__['lifecycle_rules'] = lifecycle_rules

        __props__['loggings'] = loggings

        __props__['policy'] = policy

        __props__['region'] = region

        __props__['replication_configuration'] = replication_configuration

        __props__['request_payer'] = request_payer

        __props__['server_side_encryption_configuration'] = server_side_encryption_configuration

        __props__['tags'] = tags

        __props__['versioning'] = versioning

        __props__['website'] = website

        __props__['website_domain'] = website_domain

        __props__['website_endpoint'] = website_endpoint

        __props__['bucket_domain_name'] = None
        __props__['bucket_regional_domain_name'] = None

        super(Bucket, __self__).__init__(
            'aws:s3/bucket:Bucket',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


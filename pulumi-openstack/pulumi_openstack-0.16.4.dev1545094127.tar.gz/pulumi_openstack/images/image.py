# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Image(pulumi.CustomResource):
    """
    Manages a V2 Image resource within OpenStack Glance.
    """
    def __init__(__self__, __name__, __opts__=None, container_format=None, disk_format=None, image_cache_path=None, image_source_url=None, local_file_path=None, min_disk_gb=None, min_ram_mb=None, name=None, properties=None, protected=None, region=None, tags=None, verify_checksum=None, visibility=None):
        """Create a Image resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not container_format:
            raise TypeError('Missing required property container_format')
        __props__['container_format'] = container_format

        if not disk_format:
            raise TypeError('Missing required property disk_format')
        __props__['disk_format'] = disk_format

        __props__['image_cache_path'] = image_cache_path

        __props__['image_source_url'] = image_source_url

        __props__['local_file_path'] = local_file_path

        __props__['min_disk_gb'] = min_disk_gb

        __props__['min_ram_mb'] = min_ram_mb

        __props__['name'] = name

        __props__['properties'] = properties

        __props__['protected'] = protected

        __props__['region'] = region

        __props__['tags'] = tags

        __props__['verify_checksum'] = verify_checksum

        __props__['visibility'] = visibility

        __props__['checksum'] = None
        __props__['created_at'] = None
        __props__['file'] = None
        __props__['metadata'] = None
        __props__['owner'] = None
        __props__['schema'] = None
        __props__['size_bytes'] = None
        __props__['status'] = None
        __props__['update_at'] = None

        super(Image, __self__).__init__(
            'openstack:images/image:Image',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


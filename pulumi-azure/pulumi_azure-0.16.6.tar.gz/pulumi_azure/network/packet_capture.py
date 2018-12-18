# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class PacketCapture(pulumi.CustomResource):
    """
    Configures Packet Capturing against a Virtual Machine using a Network Watcher.
    """
    def __init__(__self__, __name__, __opts__=None, filters=None, maximum_bytes_per_packet=None, maximum_bytes_per_session=None, maximum_capture_duration=None, name=None, network_watcher_name=None, resource_group_name=None, storage_location=None, target_resource_id=None):
        """Create a PacketCapture resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['filters'] = filters

        __props__['maximum_bytes_per_packet'] = maximum_bytes_per_packet

        __props__['maximum_bytes_per_session'] = maximum_bytes_per_session

        __props__['maximum_capture_duration'] = maximum_capture_duration

        __props__['name'] = name

        if not network_watcher_name:
            raise TypeError('Missing required property network_watcher_name')
        __props__['network_watcher_name'] = network_watcher_name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        if not storage_location:
            raise TypeError('Missing required property storage_location')
        __props__['storage_location'] = storage_location

        if not target_resource_id:
            raise TypeError('Missing required property target_resource_id')
        __props__['target_resource_id'] = target_resource_id

        super(PacketCapture, __self__).__init__(
            'azure:network/packetCapture:PacketCapture',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


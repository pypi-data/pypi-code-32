# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class VirtualMachine(pulumi.CustomResource):
    """
    Manages a Virtual Machine.
    
    ~> **NOTE:** Data Disks can be attached either directly on the `azurerm_virtual_machine` resource, or using the `azurerm_virtual_machine_data_disk_attachment` resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.
    """
    def __init__(__self__, __name__, __opts__=None, availability_set_id=None, boot_diagnostics=None, delete_data_disks_on_termination=None, delete_os_disk_on_termination=None, identity=None, license_type=None, location=None, name=None, network_interface_ids=None, os_profile=None, os_profile_linux_config=None, os_profile_secrets=None, os_profile_windows_config=None, plan=None, primary_network_interface_id=None, resource_group_name=None, storage_data_disks=None, storage_image_reference=None, storage_os_disk=None, tags=None, vm_size=None, zones=None):
        """Create a VirtualMachine resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['availability_set_id'] = availability_set_id

        __props__['boot_diagnostics'] = boot_diagnostics

        __props__['delete_data_disks_on_termination'] = delete_data_disks_on_termination

        __props__['delete_os_disk_on_termination'] = delete_os_disk_on_termination

        __props__['identity'] = identity

        __props__['license_type'] = license_type

        if not location:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['name'] = name

        if not network_interface_ids:
            raise TypeError('Missing required property network_interface_ids')
        __props__['network_interface_ids'] = network_interface_ids

        __props__['os_profile'] = os_profile

        __props__['os_profile_linux_config'] = os_profile_linux_config

        __props__['os_profile_secrets'] = os_profile_secrets

        __props__['os_profile_windows_config'] = os_profile_windows_config

        __props__['plan'] = plan

        __props__['primary_network_interface_id'] = primary_network_interface_id

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        __props__['resource_group_name'] = resource_group_name

        __props__['storage_data_disks'] = storage_data_disks

        __props__['storage_image_reference'] = storage_image_reference

        if not storage_os_disk:
            raise TypeError('Missing required property storage_os_disk')
        __props__['storage_os_disk'] = storage_os_disk

        __props__['tags'] = tags

        if not vm_size:
            raise TypeError('Missing required property vm_size')
        __props__['vm_size'] = vm_size

        __props__['zones'] = zones

        super(VirtualMachine, __self__).__init__(
            'azure:compute/virtualMachine:VirtualMachine',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


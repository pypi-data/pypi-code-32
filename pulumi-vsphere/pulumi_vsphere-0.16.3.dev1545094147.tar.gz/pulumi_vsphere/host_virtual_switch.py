# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities, tables

class HostVirtualSwitch(pulumi.CustomResource):
    """
    The `vsphere_host_virtual_switch` resource can be used to manage vSphere
    standard switches on an ESXi host. These switches can be used as a backing for
    standard port groups, which can be managed by the
    [`vsphere_host_port_group`][host-port-group] resource.
    
    For an overview on vSphere networking concepts, see [this
    page][ref-vsphere-net-concepts].
    
    [host-port-group]: /docs/providers/vsphere/r/host_port_group.html
    [ref-vsphere-net-concepts]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.networking.doc/GUID-2B11DBB8-CB3C-4AFF-8885-EFEA0FC562F4.html
    """
    def __init__(__self__, __name__, __opts__=None, active_nics=None, allow_forged_transmits=None, allow_mac_changes=None, allow_promiscuous=None, beacon_interval=None, check_beacon=None, failback=None, host_system_id=None, link_discovery_operation=None, link_discovery_protocol=None, mtu=None, name=None, network_adapters=None, notify_switches=None, number_of_ports=None, shaping_average_bandwidth=None, shaping_burst_size=None, shaping_enabled=None, shaping_peak_bandwidth=None, standby_nics=None, teaming_policy=None):
        """Create a HostVirtualSwitch resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not active_nics:
            raise TypeError('Missing required property active_nics')
        __props__['active_nics'] = active_nics

        __props__['allow_forged_transmits'] = allow_forged_transmits

        __props__['allow_mac_changes'] = allow_mac_changes

        __props__['allow_promiscuous'] = allow_promiscuous

        __props__['beacon_interval'] = beacon_interval

        __props__['check_beacon'] = check_beacon

        __props__['failback'] = failback

        if not host_system_id:
            raise TypeError('Missing required property host_system_id')
        __props__['host_system_id'] = host_system_id

        __props__['link_discovery_operation'] = link_discovery_operation

        __props__['link_discovery_protocol'] = link_discovery_protocol

        __props__['mtu'] = mtu

        __props__['name'] = name

        if not network_adapters:
            raise TypeError('Missing required property network_adapters')
        __props__['network_adapters'] = network_adapters

        __props__['notify_switches'] = notify_switches

        __props__['number_of_ports'] = number_of_ports

        __props__['shaping_average_bandwidth'] = shaping_average_bandwidth

        __props__['shaping_burst_size'] = shaping_burst_size

        __props__['shaping_enabled'] = shaping_enabled

        __props__['shaping_peak_bandwidth'] = shaping_peak_bandwidth

        if not standby_nics:
            raise TypeError('Missing required property standby_nics')
        __props__['standby_nics'] = standby_nics

        __props__['teaming_policy'] = teaming_policy

        super(HostVirtualSwitch, __self__).__init__(
            'vsphere:index/hostVirtualSwitch:HostVirtualSwitch',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


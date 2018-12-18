# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetRouterResult(object):
    """
    A collection of values returned by getRouter.
    """
    def __init__(__self__, availability_zone_hints=None, enable_snat=None, external_fixed_ips=None, external_network_id=None, id=None):
        if availability_zone_hints and not isinstance(availability_zone_hints, list):
            raise TypeError('Expected argument availability_zone_hints to be a list')
        __self__.availability_zone_hints = availability_zone_hints
        """
        The availability zone that is used to make router resources highly available.
        """
        if enable_snat and not isinstance(enable_snat, bool):
            raise TypeError('Expected argument enable_snat to be a bool')
        __self__.enable_snat = enable_snat
        """
        The value that points out if the Source NAT is enabled on the router.
        """
        if external_fixed_ips and not isinstance(external_fixed_ips, list):
            raise TypeError('Expected argument external_fixed_ips to be a list')
        __self__.external_fixed_ips = external_fixed_ips
        """
        The external fixed IPs of the router.
        """
        if external_network_id and not isinstance(external_network_id, str):
            raise TypeError('Expected argument external_network_id to be a str')
        __self__.external_network_id = external_network_id
        """
        The network UUID of an external gateway for the router.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_router(admin_state_up=None, distributed=None, enable_snat=None, name=None, region=None, router_id=None, status=None, tenant_id=None):
    """
    Use this data source to get the ID of an available OpenStack router.
    """
    __args__ = dict()

    __args__['adminStateUp'] = admin_state_up
    __args__['distributed'] = distributed
    __args__['enableSnat'] = enable_snat
    __args__['name'] = name
    __args__['region'] = region
    __args__['routerId'] = router_id
    __args__['status'] = status
    __args__['tenantId'] = tenant_id
    __ret__ = await pulumi.runtime.invoke('openstack:networking/getRouter:getRouter', __args__)

    return GetRouterResult(
        availability_zone_hints=__ret__.get('availabilityZoneHints'),
        enable_snat=__ret__.get('enableSnat'),
        external_fixed_ips=__ret__.get('externalFixedIps'),
        external_network_id=__ret__.get('externalNetworkId'),
        id=__ret__.get('id'))

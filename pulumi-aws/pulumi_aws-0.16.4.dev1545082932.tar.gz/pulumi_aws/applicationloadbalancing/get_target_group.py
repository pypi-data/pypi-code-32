# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetTargetGroupResult(object):
    """
    A collection of values returned by getTargetGroup.
    """
    def __init__(__self__, arn=None, arn_suffix=None, deregistration_delay=None, health_check=None, name=None, port=None, protocol=None, slow_start=None, stickiness=None, tags=None, vpc_id=None, id=None):
        if arn and not isinstance(arn, str):
            raise TypeError('Expected argument arn to be a str')
        __self__.arn = arn
        if arn_suffix and not isinstance(arn_suffix, str):
            raise TypeError('Expected argument arn_suffix to be a str')
        __self__.arn_suffix = arn_suffix
        if deregistration_delay and not isinstance(deregistration_delay, int):
            raise TypeError('Expected argument deregistration_delay to be a int')
        __self__.deregistration_delay = deregistration_delay
        if health_check and not isinstance(health_check, dict):
            raise TypeError('Expected argument health_check to be a dict')
        __self__.health_check = health_check
        if name and not isinstance(name, str):
            raise TypeError('Expected argument name to be a str')
        __self__.name = name
        if port and not isinstance(port, int):
            raise TypeError('Expected argument port to be a int')
        __self__.port = port
        if protocol and not isinstance(protocol, str):
            raise TypeError('Expected argument protocol to be a str')
        __self__.protocol = protocol
        if slow_start and not isinstance(slow_start, int):
            raise TypeError('Expected argument slow_start to be a int')
        __self__.slow_start = slow_start
        if stickiness and not isinstance(stickiness, dict):
            raise TypeError('Expected argument stickiness to be a dict')
        __self__.stickiness = stickiness
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError('Expected argument vpc_id to be a str')
        __self__.vpc_id = vpc_id
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_target_group(arn=None, name=None, tags=None):
    """
    ~> **Note:** `aws_alb_target_group` is known as `aws_lb_target_group`. The functionality is identical.
    
    Provides information about a Load Balancer Target Group.
    
    This data source can prove useful when a module accepts an LB Target Group as an
    input variable and needs to know its attributes. It can also be used to get the ARN of
    an LB Target Group for use in other resources, given LB Target Group name.
    """
    __args__ = dict()

    __args__['arn'] = arn
    __args__['name'] = name
    __args__['tags'] = tags
    __ret__ = await pulumi.runtime.invoke('aws:applicationloadbalancing/getTargetGroup:getTargetGroup', __args__)

    return GetTargetGroupResult(
        arn=__ret__.get('arn'),
        arn_suffix=__ret__.get('arnSuffix'),
        deregistration_delay=__ret__.get('deregistrationDelay'),
        health_check=__ret__.get('healthCheck'),
        name=__ret__.get('name'),
        port=__ret__.get('port'),
        protocol=__ret__.get('protocol'),
        slow_start=__ret__.get('slowStart'),
        stickiness=__ret__.get('stickiness'),
        tags=__ret__.get('tags'),
        vpc_id=__ret__.get('vpcId'),
        id=__ret__.get('id'))

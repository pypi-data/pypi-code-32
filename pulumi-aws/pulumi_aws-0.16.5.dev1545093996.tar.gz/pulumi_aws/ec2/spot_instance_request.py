# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class SpotInstanceRequest(pulumi.CustomResource):
    """
    Provides an EC2 Spot Instance Request resource. This allows instances to be
    requested on the spot market.
    
    By default Terraform creates Spot Instance Requests with a `persistent` type,
    which means that for the duration of their lifetime, AWS will launch an
    instance with the configured details if and when the spot market will accept
    the requested price.
    
    On destruction, Terraform will make an attempt to terminate the associated Spot
    Instance if there is one present.
    
    Spot Instances requests with a `one-time` type will close the spot request
    when the instance is terminated either by the request being below the current spot
    price availability or by a user.
    
    ~> **NOTE:** Because their behavior depends on the live status of the spot
    market, Spot Instance Requests have a unique lifecycle that makes them behave
    differently than other Terraform resources. Most importantly: there is __no
    guarantee__ that a Spot Instance exists to fulfill the request at any given
    point in time. See the [AWS Spot Instance
    documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
    for more information.
    
    """
    def __init__(__self__, __name__, __opts__=None, ami=None, associate_public_ip_address=None, availability_zone=None, block_duration_minutes=None, cpu_core_count=None, cpu_threads_per_core=None, credit_specification=None, disable_api_termination=None, ebs_block_devices=None, ebs_optimized=None, ephemeral_block_devices=None, get_password_data=None, host_id=None, iam_instance_profile=None, instance_initiated_shutdown_behavior=None, instance_interruption_behaviour=None, instance_type=None, ipv6_address_count=None, ipv6_addresses=None, key_name=None, launch_group=None, monitoring=None, network_interfaces=None, placement_group=None, private_ip=None, root_block_device=None, security_groups=None, source_dest_check=None, spot_price=None, spot_type=None, subnet_id=None, tags=None, tenancy=None, user_data=None, user_data_base64=None, valid_from=None, valid_until=None, volume_tags=None, vpc_security_group_ids=None, wait_for_fulfillment=None):
        """Create a SpotInstanceRequest resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not ami:
            raise TypeError('Missing required property ami')
        __props__['ami'] = ami

        __props__['associate_public_ip_address'] = associate_public_ip_address

        __props__['availability_zone'] = availability_zone

        __props__['block_duration_minutes'] = block_duration_minutes

        __props__['cpu_core_count'] = cpu_core_count

        __props__['cpu_threads_per_core'] = cpu_threads_per_core

        __props__['credit_specification'] = credit_specification

        __props__['disable_api_termination'] = disable_api_termination

        __props__['ebs_block_devices'] = ebs_block_devices

        __props__['ebs_optimized'] = ebs_optimized

        __props__['ephemeral_block_devices'] = ephemeral_block_devices

        __props__['get_password_data'] = get_password_data

        __props__['host_id'] = host_id

        __props__['iam_instance_profile'] = iam_instance_profile

        __props__['instance_initiated_shutdown_behavior'] = instance_initiated_shutdown_behavior

        __props__['instance_interruption_behaviour'] = instance_interruption_behaviour

        if not instance_type:
            raise TypeError('Missing required property instance_type')
        __props__['instance_type'] = instance_type

        __props__['ipv6_address_count'] = ipv6_address_count

        __props__['ipv6_addresses'] = ipv6_addresses

        __props__['key_name'] = key_name

        __props__['launch_group'] = launch_group

        __props__['monitoring'] = monitoring

        __props__['network_interfaces'] = network_interfaces

        __props__['placement_group'] = placement_group

        __props__['private_ip'] = private_ip

        __props__['root_block_device'] = root_block_device

        __props__['security_groups'] = security_groups

        __props__['source_dest_check'] = source_dest_check

        __props__['spot_price'] = spot_price

        __props__['spot_type'] = spot_type

        __props__['subnet_id'] = subnet_id

        __props__['tags'] = tags

        __props__['tenancy'] = tenancy

        __props__['user_data'] = user_data

        __props__['user_data_base64'] = user_data_base64

        __props__['valid_from'] = valid_from

        __props__['valid_until'] = valid_until

        __props__['volume_tags'] = volume_tags

        __props__['vpc_security_group_ids'] = vpc_security_group_ids

        __props__['wait_for_fulfillment'] = wait_for_fulfillment

        __props__['arn'] = None
        __props__['instance_state'] = None
        __props__['network_interface_id'] = None
        __props__['password_data'] = None
        __props__['primary_network_interface_id'] = None
        __props__['private_dns'] = None
        __props__['public_dns'] = None
        __props__['public_ip'] = None
        __props__['spot_bid_status'] = None
        __props__['spot_instance_id'] = None
        __props__['spot_request_state'] = None

        super(SpotInstanceRequest, __self__).__init__(
            'aws:ec2/spotInstanceRequest:SpotInstanceRequest',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


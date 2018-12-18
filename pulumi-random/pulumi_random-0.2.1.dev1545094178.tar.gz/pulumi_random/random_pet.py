# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities, tables

class RandomPet(pulumi.CustomResource):
    """
    The resource `random_pet` generates random pet names that are intended to be
    used as unique identifiers for other resources.
    
    This resource can be used in conjunction with resources that have
    the `create_before_destroy` lifecycle flag set, to avoid conflicts with
    unique names during the brief period where both the old and new resources
    exist concurrently.
    """
    def __init__(__self__, __name__, __opts__=None, keepers=None, length=None, prefix=None, separator=None):
        """Create a RandomPet resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['keepers'] = keepers

        __props__['length'] = length

        __props__['prefix'] = prefix

        __props__['separator'] = separator

        super(RandomPet, __self__).__init__(
            'random:index/randomPet:RandomPet',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


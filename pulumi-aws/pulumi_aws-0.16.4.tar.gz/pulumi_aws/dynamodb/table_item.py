# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class TableItem(pulumi.CustomResource):
    """
    Provides a DynamoDB table item resource
    
    -> **Note:** This resource is not meant to be used for managing large amounts of data in your table, it is not designed to scale.
      You should perform **regular backups** of all data in the table, see [AWS docs for more](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html).
    """
    def __init__(__self__, __name__, __opts__=None, hash_key=None, item=None, range_key=None, table_name=None):
        """Create a TableItem resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not hash_key:
            raise TypeError('Missing required property hash_key')
        __props__['hash_key'] = hash_key

        if not item:
            raise TypeError('Missing required property item')
        __props__['item'] = item

        __props__['range_key'] = range_key

        if not table_name:
            raise TypeError('Missing required property table_name')
        __props__['table_name'] = table_name

        super(TableItem, __self__).__init__(
            'aws:dynamodb/tableItem:TableItem',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


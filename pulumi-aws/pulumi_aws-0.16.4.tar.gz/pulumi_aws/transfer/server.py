# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class Server(pulumi.CustomResource):
    """
    Provides a AWS Transfer Server resource.
    
    
    ```hcl
    resource "aws_iam_role" "foo" {
    	name = "tf-test-transfer-server-iam-role"
      
    	assume_role_policy = <<EOF
    {
    	"Version": "2012-10-17",
    	"Statement": [
    		{
    		"Effect": "Allow",
    		"Principal": {
    			"Service": "transfer.amazonaws.com"
    		},
    		"Action": "sts:AssumeRole"
    		}
    	]
    }
    EOF
    }
    
    resource "aws_iam_role_policy" "foo" {
    	name = "tf-test-transfer-server-iam-policy-%s"
    	role = "${aws_iam_role.foo.id}"
    	policy = <<POLICY
    {
    	"Version": "2012-10-17",
    	"Statement": [
    		{
    		"Sid": "AllowFullAccesstoCloudWatchLogs",
    		"Effect": "Allow",
    		"Action": [
    			"logs:*"
    		],
    		"Resource": "*"
    		}
    	]
    }
    POLICY
    }
    
    
    resource "aws_transfer_server" "foo" {
      identity_provider_type = "SERVICE_MANAGED"
      logging_role = "${aws_iam_role.foo.arn}"
    
      tags {
    	NAME   = "tf-acc-test-transfer-server"
    	ENV    = "test"
      }
    }
    ```
    """
    def __init__(__self__, __name__, __opts__=None, identity_provider_type=None, invocation_role=None, logging_role=None, tags=None, url=None):
        """Create a Server resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['identity_provider_type'] = identity_provider_type

        __props__['invocation_role'] = invocation_role

        __props__['logging_role'] = logging_role

        __props__['tags'] = tags

        __props__['url'] = url

        __props__['arn'] = None
        __props__['endpoint'] = None

        super(Server, __self__).__init__(
            'aws:transfer/server:Server',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


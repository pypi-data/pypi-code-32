# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetIAMPolicyResult(object):
    """
    A collection of values returned by getIAMPolicy.
    """
    def __init__(__self__, policy_data=None, id=None):
        if policy_data and not isinstance(policy_data, str):
            raise TypeError('Expected argument policy_data to be a str')
        __self__.policy_data = policy_data
        """
        The above bindings serialized in a format suitable for
        referencing from a resource that supports IAM.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_iam_policy(bindings=None):
    """
    Generates an IAM policy document that may be referenced by and applied to
    other Google Cloud Platform resources, such as the `google_project` resource.
    
    ```
    data "google_iam_policy" "admin" {
      binding {
        role = "roles/compute.instanceAdmin"
    
        members = [
          "serviceAccount:your-custom-sa@your-project.iam.gserviceaccount.com",
        ]
      }
    
      binding {
        role = "roles/storage.objectViewer"
    
        members = [
          "user:jane@example.com",
        ]
      }
    }
    ```
    
    This data source is used to define IAM policies to apply to other resources.
    Currently, defining a policy through a datasource and referencing that policy
    from another resource is the only way to apply an IAM policy to a resource.
    
    **Note:** Several restrictions apply when setting IAM policies through this API.
    See the [setIamPolicy docs](https://cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)
    for a list of these restrictions.
    """
    __args__ = dict()

    __args__['bindings'] = bindings
    __ret__ = await pulumi.runtime.invoke('gcp:organizations/getIAMPolicy:getIAMPolicy', __args__)

    return GetIAMPolicyResult(
        policy_data=__ret__.get('policyData'),
        id=__ret__.get('id'))

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetProjectServiceAccountResult(object):
    """
    A collection of values returned by getProjectServiceAccount.
    """
    def __init__(__self__, email_address=None, project=None, id=None):
        if email_address and not isinstance(email_address, str):
            raise TypeError('Expected argument email_address to be a str')
        __self__.email_address = email_address
        """
        The email address of the service account. This value is often used to refer to the service account
        in order to grant IAM permissions.
        """
        if project and not isinstance(project, str):
            raise TypeError('Expected argument project to be a str')
        __self__.project = project
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_project_service_account(project=None, user_project=None):
    """
    Get the email address of a project's unique Google Cloud Storage service account.
    
    Each Google Cloud project has a unique service account for use with Google Cloud Storage. Only this
    special service account can be used to set up `google_storage_notification` resources.
    
    For more information see
    [the API reference](https://cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount).
    """
    __args__ = dict()

    __args__['project'] = project
    __args__['userProject'] = user_project
    __ret__ = await pulumi.runtime.invoke('gcp:storage/getProjectServiceAccount:getProjectServiceAccount', __args__)

    return GetProjectServiceAccountResult(
        email_address=__ret__.get('emailAddress'),
        project=__ret__.get('project'),
        id=__ret__.get('id'))

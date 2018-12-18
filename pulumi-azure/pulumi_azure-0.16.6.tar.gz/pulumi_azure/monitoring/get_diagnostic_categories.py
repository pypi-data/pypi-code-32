# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetDiagnosticCategoriesResult(object):
    """
    A collection of values returned by getDiagnosticCategories.
    """
    def __init__(__self__, logs=None, metrics=None, id=None):
        if logs and not isinstance(logs, list):
            raise TypeError('Expected argument logs to be a list')
        __self__.logs = logs
        """
        A list of the Log Categories supported for this Resource.
        """
        if metrics and not isinstance(metrics, list):
            raise TypeError('Expected argument metrics to be a list')
        __self__.metrics = metrics
        """
        A list of the Metric Categories supported for this Resource.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_diagnostic_categories(resource_id=None):
    """
    Use this data source to access information about the Monitor Diagnostics Categories supported by an existing Resource.
    """
    __args__ = dict()

    __args__['resourceId'] = resource_id
    __ret__ = await pulumi.runtime.invoke('azure:monitoring/getDiagnosticCategories:getDiagnosticCategories', __args__)

    return GetDiagnosticCategoriesResult(
        logs=__ret__.get('logs'),
        metrics=__ret__.get('metrics'),
        id=__ret__.get('id'))

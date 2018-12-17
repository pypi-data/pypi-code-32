# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LogicalDeviceSearch(Model):
    """LogicalDeviceSearch.

    :param logical_devices: An array of logical devices returned by the search
    :type logical_devices:
     list[~energycap.sdk.models.RouteSearchLogicalDevice]
    :param places: An array of places returned by the search
    :type places: list[~energycap.sdk.models.RouteSearchPlace]
    """

    _attribute_map = {
        'logical_devices': {'key': 'logicalDevices', 'type': '[RouteSearchLogicalDevice]'},
        'places': {'key': 'places', 'type': '[RouteSearchPlace]'},
    }

    def __init__(self, logical_devices=None, places=None):
        super(LogicalDeviceSearch, self).__init__()
        self.logical_devices = logical_devices
        self.places = places

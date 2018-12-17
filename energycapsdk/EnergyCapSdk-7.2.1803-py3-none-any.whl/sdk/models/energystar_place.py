# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class EnergystarPlace(Model):
    """EnergystarPlace.

    :param place: The building
    :type place: ~energycap.sdk.models.PlaceChild
    :param address: The address for the building
    :type address: ~energycap.sdk.models.AddressChild
    :param energystar_rating: The current ENERGY STAR rating
    :type energystar_rating: int
    :param energystar_rating_date: The date that the building received the
     current ENERGY STAR rating
    :type energystar_rating_date: datetime
    :param is_energystar_turned_on: Whether or not ENERGY STAR submissions are
     enabled for the building
    :type is_energystar_turned_on: bool
    :param current_area: Current floor area value for the building
    :type current_area: int
    :param current_area_unit: Current floor area unit for the building
    :type current_area_unit: str
    """

    _attribute_map = {
        'place': {'key': 'place', 'type': 'PlaceChild'},
        'address': {'key': 'address', 'type': 'AddressChild'},
        'energystar_rating': {'key': 'energystarRating', 'type': 'int'},
        'energystar_rating_date': {'key': 'energystarRatingDate', 'type': 'iso-8601'},
        'is_energystar_turned_on': {'key': 'isEnergystarTurnedOn', 'type': 'bool'},
        'current_area': {'key': 'currentArea', 'type': 'int'},
        'current_area_unit': {'key': 'currentAreaUnit', 'type': 'str'},
    }

    def __init__(self, place=None, address=None, energystar_rating=None, energystar_rating_date=None, is_energystar_turned_on=None, current_area=None, current_area_unit=None):
        super(EnergystarPlace, self).__init__()
        self.place = place
        self.address = address
        self.energystar_rating = energystar_rating
        self.energystar_rating_date = energystar_rating_date
        self.is_energystar_turned_on = is_energystar_turned_on
        self.current_area = current_area
        self.current_area_unit = current_area_unit

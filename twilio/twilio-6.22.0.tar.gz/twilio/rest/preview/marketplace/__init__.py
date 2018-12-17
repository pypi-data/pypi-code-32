# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.preview.marketplace.available_add_on import AvailableAddOnList
from twilio.rest.preview.marketplace.installed_add_on import InstalledAddOnList


class Marketplace(Version):

    def __init__(self, domain):
        """
        Initialize the Marketplace version of Preview

        :returns: Marketplace version of Preview
        :rtype: twilio.rest.preview.marketplace.Marketplace.Marketplace
        """
        super(Marketplace, self).__init__(domain)
        self.version = 'marketplace'
        self._installed_add_ons = None
        self._available_add_ons = None

    @property
    def installed_add_ons(self):
        """
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnList
        """
        if self._installed_add_ons is None:
            self._installed_add_ons = InstalledAddOnList(self)
        return self._installed_add_ons

    @property
    def available_add_ons(self):
        """
        :rtype: twilio.rest.preview.marketplace.available_add_on.AvailableAddOnList
        """
        if self._available_add_ons is None:
            self._available_add_ons = AvailableAddOnList(self)
        return self._available_add_ons

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace>'

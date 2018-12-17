# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class SettingsList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the SettingsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.permissions.voice_permission.settings.SettingsList
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsList
        """
        super(SettingsList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a SettingsContext

        :returns: twilio.rest.preview.permissions.voice_permission.settings.SettingsContext
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsContext
        """
        return SettingsContext(self._version, )

    def __call__(self):
        """
        Constructs a SettingsContext

        :returns: twilio.rest.preview.permissions.voice_permission.settings.SettingsContext
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsContext
        """
        return SettingsContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Permissions.SettingsList>'


class SettingsPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the SettingsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.permissions.voice_permission.settings.SettingsPage
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsPage
        """
        super(SettingsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of SettingsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.permissions.voice_permission.settings.SettingsInstance
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsInstance
        """
        return SettingsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Permissions.SettingsPage>'


class SettingsContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the SettingsContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.permissions.voice_permission.settings.SettingsContext
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsContext
        """
        super(SettingsContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/VoicePermissions/Settings'.format(**self._solution)

    def fetch(self):
        """
        Fetch a SettingsInstance

        :returns: Fetched SettingsInstance
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return SettingsInstance(self._version, payload, )

    def update(self, inheritance=values.unset):
        """
        Update the SettingsInstance

        :param bool inheritance: Set true to enable inheritance voice permissions settings, false to disable

        :returns: Updated SettingsInstance
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsInstance
        """
        data = values.of({'Inheritance': inheritance, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return SettingsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Permissions.SettingsContext {}>'.format(context)


class SettingsInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload):
        """
        Initialize the SettingsInstance

        :returns: twilio.rest.preview.permissions.voice_permission.settings.SettingsInstance
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsInstance
        """
        super(SettingsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {'inheritance': payload['inheritance'], 'url': payload['url'], }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: SettingsContext for this SettingsInstance
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsContext
        """
        if self._context is None:
            self._context = SettingsContext(self._version, )
        return self._context

    @property
    def inheritance(self):
        """
        :returns: The status of  inheritance of outbound voice permissions and blocklist
        :rtype: bool
        """
        return self._properties['inheritance']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a SettingsInstance

        :returns: Fetched SettingsInstance
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsInstance
        """
        return self._proxy.fetch()

    def update(self, inheritance=values.unset):
        """
        Update the SettingsInstance

        :param bool inheritance: Set true to enable inheritance voice permissions settings, false to disable

        :returns: Updated SettingsInstance
        :rtype: twilio.rest.preview.permissions.voice_permission.settings.SettingsInstance
        """
        return self._proxy.update(inheritance=inheritance, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Permissions.SettingsInstance {}>'.format(context)

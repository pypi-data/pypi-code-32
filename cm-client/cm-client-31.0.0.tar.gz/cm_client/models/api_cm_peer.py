# coding: utf-8

"""
    Cloudera Manager API

    <h1>Cloudera Manager API v31</h1>       <p>Introduced in Cloudera Manager 6.1.0</p>       <p><a href=\"http://www.cloudera.com/documentation.html\">Cloudera Product Documentation</a></p>

    OpenAPI spec version: 6.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ApiCmPeer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'type': 'ApiCmPeerType',
        'url': 'str',
        'username': 'str',
        'password': 'str',
        'cloudera_manager_created_user': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'url': 'url',
        'username': 'username',
        'password': 'password',
        'cloudera_manager_created_user': 'clouderaManagerCreatedUser'
    }

    def __init__(self, name=None, type=None, url=None, username=None, password=None, cloudera_manager_created_user=None):
        """
        ApiCmPeer - a model defined in Swagger
        """

        self._name = None
        self._type = None
        self._url = None
        self._username = None
        self._password = None
        self._cloudera_manager_created_user = None

        if name is not None:
          self.name = name
        if type is not None:
          self.type = type
        if url is not None:
          self.url = url
        if username is not None:
          self.username = username
        if password is not None:
          self.password = password
        if cloudera_manager_created_user is not None:
          self.cloudera_manager_created_user = cloudera_manager_created_user

    @property
    def name(self):
        """
        Gets the name of this ApiCmPeer.
        The name of the remote CM instance. Immutable during update.

        :return: The name of this ApiCmPeer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApiCmPeer.
        The name of the remote CM instance. Immutable during update.

        :param name: The name of this ApiCmPeer.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this ApiCmPeer.
        The type of the remote CM instance. Immutable during update.  Available since API v11.

        :return: The type of this ApiCmPeer.
        :rtype: ApiCmPeerType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApiCmPeer.
        The type of the remote CM instance. Immutable during update.  Available since API v11.

        :param type: The type of this ApiCmPeer.
        :type: ApiCmPeerType
        """

        self._type = type

    @property
    def url(self):
        """
        Gets the url of this ApiCmPeer.
        The URL of the remote CM instance. Mutable during update.

        :return: The url of this ApiCmPeer.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this ApiCmPeer.
        The URL of the remote CM instance. Mutable during update.

        :param url: The url of this ApiCmPeer.
        :type: str
        """

        self._url = url

    @property
    def username(self):
        """
        Gets the username of this ApiCmPeer.
        When creating peers, if 'clouderaManagerCreatedUser' is true, this should be the remote admin username for creating a user in remote Cloudera Manager. The created remote user will then be stored in the local Cloudera Manager DB and used in later communication. If 'clouderaManagerCreatedUser' is false, which is not applicable to REPLICATION peer type, Cloudera Manager will store this username in the local DB directly and use it together with 'password' for communication.  Mutable during update. When set during update, if 'clouderaManagerCreatedUser' is true, a new user in remote Cloudera Manager is created, the newly created remote user will be stored in the local DB. An attempt to delete the previously created remote user will be made; If 'clouderaManagerCreatedUser' is false, the username/password in the local DB will be updated.

        :return: The username of this ApiCmPeer.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this ApiCmPeer.
        When creating peers, if 'clouderaManagerCreatedUser' is true, this should be the remote admin username for creating a user in remote Cloudera Manager. The created remote user will then be stored in the local Cloudera Manager DB and used in later communication. If 'clouderaManagerCreatedUser' is false, which is not applicable to REPLICATION peer type, Cloudera Manager will store this username in the local DB directly and use it together with 'password' for communication.  Mutable during update. When set during update, if 'clouderaManagerCreatedUser' is true, a new user in remote Cloudera Manager is created, the newly created remote user will be stored in the local DB. An attempt to delete the previously created remote user will be made; If 'clouderaManagerCreatedUser' is false, the username/password in the local DB will be updated.

        :param username: The username of this ApiCmPeer.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this ApiCmPeer.
        When creating peers, if 'clouderaManagerCreatedUser' is true, this should be the remote admin password for creating a user in remote Cloudera Manager. The created remote user will then be stored in the local Cloudera Manager DB and used in later communication. If 'clouderaManagerCreatedUser' is false, which is not applicable to REPLICATION peer type, Cloudera Manager will store this password in the local DB directly and use it together with 'username' for communication.  Mutable during update. When set during update, if 'clouderaManagerCreatedUser' is true, a new user in remote Cloudera Manager is created, the newly created remote user will be stored in the local DB. An attempt to delete the previously created remote user will be made; If 'clouderaManagerCreatedUser' is false, the username/password in the local DB will be updated.

        :return: The password of this ApiCmPeer.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ApiCmPeer.
        When creating peers, if 'clouderaManagerCreatedUser' is true, this should be the remote admin password for creating a user in remote Cloudera Manager. The created remote user will then be stored in the local Cloudera Manager DB and used in later communication. If 'clouderaManagerCreatedUser' is false, which is not applicable to REPLICATION peer type, Cloudera Manager will store this password in the local DB directly and use it together with 'username' for communication.  Mutable during update. When set during update, if 'clouderaManagerCreatedUser' is true, a new user in remote Cloudera Manager is created, the newly created remote user will be stored in the local DB. An attempt to delete the previously created remote user will be made; If 'clouderaManagerCreatedUser' is false, the username/password in the local DB will be updated.

        :param password: The password of this ApiCmPeer.
        :type: str
        """

        self._password = password

    @property
    def cloudera_manager_created_user(self):
        """
        Gets the cloudera_manager_created_user of this ApiCmPeer.
        If true, Cloudera Manager creates a remote user using the given username/password and stores the created user in local DB for use in later communication. Cloudera Manager will also try to delete the created remote user when deleting such peers.  If false, Cloudera Manager will store the provided username/password in the local DB and use them in later communication. 'false' value on this field is not applicable to REPLICATION peer type.  Available since API v11.  Immutable during update. Should not be set when updating peers.

        :return: The cloudera_manager_created_user of this ApiCmPeer.
        :rtype: bool
        """
        return self._cloudera_manager_created_user

    @cloudera_manager_created_user.setter
    def cloudera_manager_created_user(self, cloudera_manager_created_user):
        """
        Sets the cloudera_manager_created_user of this ApiCmPeer.
        If true, Cloudera Manager creates a remote user using the given username/password and stores the created user in local DB for use in later communication. Cloudera Manager will also try to delete the created remote user when deleting such peers.  If false, Cloudera Manager will store the provided username/password in the local DB and use them in later communication. 'false' value on this field is not applicable to REPLICATION peer type.  Available since API v11.  Immutable during update. Should not be set when updating peers.

        :param cloudera_manager_created_user: The cloudera_manager_created_user of this ApiCmPeer.
        :type: bool
        """

        self._cloudera_manager_created_user = cloudera_manager_created_user

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ApiCmPeer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

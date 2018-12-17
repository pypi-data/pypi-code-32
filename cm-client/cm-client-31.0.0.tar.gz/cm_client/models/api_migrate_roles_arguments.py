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


class ApiMigrateRolesArguments(object):
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
        'role_names_to_migrate': 'list[str]',
        'destination_host_id': 'str',
        'clear_stale_role_data': 'bool'
    }

    attribute_map = {
        'role_names_to_migrate': 'roleNamesToMigrate',
        'destination_host_id': 'destinationHostId',
        'clear_stale_role_data': 'clearStaleRoleData'
    }

    def __init__(self, role_names_to_migrate=None, destination_host_id=None, clear_stale_role_data=None):
        """
        ApiMigrateRolesArguments - a model defined in Swagger
        """

        self._role_names_to_migrate = None
        self._destination_host_id = None
        self._clear_stale_role_data = None

        if role_names_to_migrate is not None:
          self.role_names_to_migrate = role_names_to_migrate
        if destination_host_id is not None:
          self.destination_host_id = destination_host_id
        if clear_stale_role_data is not None:
          self.clear_stale_role_data = clear_stale_role_data

    @property
    def role_names_to_migrate(self):
        """
        Gets the role_names_to_migrate of this ApiMigrateRolesArguments.
        The list of role names to migrate.

        :return: The role_names_to_migrate of this ApiMigrateRolesArguments.
        :rtype: list[str]
        """
        return self._role_names_to_migrate

    @role_names_to_migrate.setter
    def role_names_to_migrate(self, role_names_to_migrate):
        """
        Sets the role_names_to_migrate of this ApiMigrateRolesArguments.
        The list of role names to migrate.

        :param role_names_to_migrate: The role_names_to_migrate of this ApiMigrateRolesArguments.
        :type: list[str]
        """

        self._role_names_to_migrate = role_names_to_migrate

    @property
    def destination_host_id(self):
        """
        Gets the destination_host_id of this ApiMigrateRolesArguments.
        The ID of the host to which the roles should be migrated.

        :return: The destination_host_id of this ApiMigrateRolesArguments.
        :rtype: str
        """
        return self._destination_host_id

    @destination_host_id.setter
    def destination_host_id(self, destination_host_id):
        """
        Sets the destination_host_id of this ApiMigrateRolesArguments.
        The ID of the host to which the roles should be migrated.

        :param destination_host_id: The destination_host_id of this ApiMigrateRolesArguments.
        :type: str
        """

        self._destination_host_id = destination_host_id

    @property
    def clear_stale_role_data(self):
        """
        Gets the clear_stale_role_data of this ApiMigrateRolesArguments.
        Delete existing stale role data, if any. For example, when migrating a NameNode, if the destination host has stale data in the NameNode data directories (possibly because a NameNode role was previously located there), this stale data will be deleted before migrating the role.

        :return: The clear_stale_role_data of this ApiMigrateRolesArguments.
        :rtype: bool
        """
        return self._clear_stale_role_data

    @clear_stale_role_data.setter
    def clear_stale_role_data(self, clear_stale_role_data):
        """
        Sets the clear_stale_role_data of this ApiMigrateRolesArguments.
        Delete existing stale role data, if any. For example, when migrating a NameNode, if the destination host has stale data in the NameNode data directories (possibly because a NameNode role was previously located there), this stale data will be deleted before migrating the role.

        :param clear_stale_role_data: The clear_stale_role_data of this ApiMigrateRolesArguments.
        :type: bool
        """

        self._clear_stale_role_data = clear_stale_role_data

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
        if not isinstance(other, ApiMigrateRolesArguments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

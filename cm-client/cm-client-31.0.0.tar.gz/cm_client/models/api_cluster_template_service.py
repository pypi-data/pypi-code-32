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


class ApiClusterTemplateService(object):
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
        'ref_name': 'str',
        'service_type': 'str',
        'service_configs': 'list[ApiClusterTemplateConfig]',
        'role_config_groups': 'list[ApiClusterTemplateRoleConfigGroup]',
        'roles': 'list[ApiClusterTemplateRole]',
        'display_name': 'str'
    }

    attribute_map = {
        'ref_name': 'refName',
        'service_type': 'serviceType',
        'service_configs': 'serviceConfigs',
        'role_config_groups': 'roleConfigGroups',
        'roles': 'roles',
        'display_name': 'displayName'
    }

    def __init__(self, ref_name=None, service_type=None, service_configs=None, role_config_groups=None, roles=None, display_name=None):
        """
        ApiClusterTemplateService - a model defined in Swagger
        """

        self._ref_name = None
        self._service_type = None
        self._service_configs = None
        self._role_config_groups = None
        self._roles = None
        self._display_name = None

        if ref_name is not None:
          self.ref_name = ref_name
        if service_type is not None:
          self.service_type = service_type
        if service_configs is not None:
          self.service_configs = service_configs
        if role_config_groups is not None:
          self.role_config_groups = role_config_groups
        if roles is not None:
          self.roles = roles
        if display_name is not None:
          self.display_name = display_name

    @property
    def ref_name(self):
        """
        Gets the ref_name of this ApiClusterTemplateService.
        

        :return: The ref_name of this ApiClusterTemplateService.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        """
        Sets the ref_name of this ApiClusterTemplateService.
        

        :param ref_name: The ref_name of this ApiClusterTemplateService.
        :type: str
        """

        self._ref_name = ref_name

    @property
    def service_type(self):
        """
        Gets the service_type of this ApiClusterTemplateService.
        

        :return: The service_type of this ApiClusterTemplateService.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """
        Sets the service_type of this ApiClusterTemplateService.
        

        :param service_type: The service_type of this ApiClusterTemplateService.
        :type: str
        """

        self._service_type = service_type

    @property
    def service_configs(self):
        """
        Gets the service_configs of this ApiClusterTemplateService.
        

        :return: The service_configs of this ApiClusterTemplateService.
        :rtype: list[ApiClusterTemplateConfig]
        """
        return self._service_configs

    @service_configs.setter
    def service_configs(self, service_configs):
        """
        Sets the service_configs of this ApiClusterTemplateService.
        

        :param service_configs: The service_configs of this ApiClusterTemplateService.
        :type: list[ApiClusterTemplateConfig]
        """

        self._service_configs = service_configs

    @property
    def role_config_groups(self):
        """
        Gets the role_config_groups of this ApiClusterTemplateService.
        

        :return: The role_config_groups of this ApiClusterTemplateService.
        :rtype: list[ApiClusterTemplateRoleConfigGroup]
        """
        return self._role_config_groups

    @role_config_groups.setter
    def role_config_groups(self, role_config_groups):
        """
        Sets the role_config_groups of this ApiClusterTemplateService.
        

        :param role_config_groups: The role_config_groups of this ApiClusterTemplateService.
        :type: list[ApiClusterTemplateRoleConfigGroup]
        """

        self._role_config_groups = role_config_groups

    @property
    def roles(self):
        """
        Gets the roles of this ApiClusterTemplateService.
        

        :return: The roles of this ApiClusterTemplateService.
        :rtype: list[ApiClusterTemplateRole]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this ApiClusterTemplateService.
        

        :param roles: The roles of this ApiClusterTemplateService.
        :type: list[ApiClusterTemplateRole]
        """

        self._roles = roles

    @property
    def display_name(self):
        """
        Gets the display_name of this ApiClusterTemplateService.
        

        :return: The display_name of this ApiClusterTemplateService.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApiClusterTemplateService.
        

        :param display_name: The display_name of this ApiClusterTemplateService.
        :type: str
        """

        self._display_name = display_name

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
        if not isinstance(other, ApiClusterTemplateService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

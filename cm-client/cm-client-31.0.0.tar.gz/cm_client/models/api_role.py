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


class ApiRole(object):
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
        'type': 'str',
        'host_ref': 'ApiHostRef',
        'service_ref': 'ApiServiceRef',
        'role_state': 'ApiRoleState',
        'commission_state': 'ApiCommissionState',
        'health_summary': 'ApiHealthSummary',
        'config_stale': 'bool',
        'config_staleness_status': 'ApiConfigStalenessStatus',
        'health_checks': 'list[ApiHealthCheck]',
        'ha_status': 'HaStatus',
        'role_url': 'str',
        'maintenance_mode': 'bool',
        'maintenance_owners': 'list[ApiEntityType]',
        'config': 'ApiConfigList',
        'role_config_group_ref': 'ApiRoleConfigGroupRef',
        'zoo_keeper_server_mode': 'ZooKeeperServerMode',
        'entity_status': 'ApiEntityStatus'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'host_ref': 'hostRef',
        'service_ref': 'serviceRef',
        'role_state': 'roleState',
        'commission_state': 'commissionState',
        'health_summary': 'healthSummary',
        'config_stale': 'configStale',
        'config_staleness_status': 'configStalenessStatus',
        'health_checks': 'healthChecks',
        'ha_status': 'haStatus',
        'role_url': 'roleUrl',
        'maintenance_mode': 'maintenanceMode',
        'maintenance_owners': 'maintenanceOwners',
        'config': 'config',
        'role_config_group_ref': 'roleConfigGroupRef',
        'zoo_keeper_server_mode': 'zooKeeperServerMode',
        'entity_status': 'entityStatus'
    }

    def __init__(self, name=None, type=None, host_ref=None, service_ref=None, role_state=None, commission_state=None, health_summary=None, config_stale=None, config_staleness_status=None, health_checks=None, ha_status=None, role_url=None, maintenance_mode=None, maintenance_owners=None, config=None, role_config_group_ref=None, zoo_keeper_server_mode=None, entity_status=None):
        """
        ApiRole - a model defined in Swagger
        """

        self._name = None
        self._type = None
        self._host_ref = None
        self._service_ref = None
        self._role_state = None
        self._commission_state = None
        self._health_summary = None
        self._config_stale = None
        self._config_staleness_status = None
        self._health_checks = None
        self._ha_status = None
        self._role_url = None
        self._maintenance_mode = None
        self._maintenance_owners = None
        self._config = None
        self._role_config_group_ref = None
        self._zoo_keeper_server_mode = None
        self._entity_status = None

        if name is not None:
          self.name = name
        if type is not None:
          self.type = type
        if host_ref is not None:
          self.host_ref = host_ref
        if service_ref is not None:
          self.service_ref = service_ref
        if role_state is not None:
          self.role_state = role_state
        if commission_state is not None:
          self.commission_state = commission_state
        if health_summary is not None:
          self.health_summary = health_summary
        if config_stale is not None:
          self.config_stale = config_stale
        if config_staleness_status is not None:
          self.config_staleness_status = config_staleness_status
        if health_checks is not None:
          self.health_checks = health_checks
        if ha_status is not None:
          self.ha_status = ha_status
        if role_url is not None:
          self.role_url = role_url
        if maintenance_mode is not None:
          self.maintenance_mode = maintenance_mode
        if maintenance_owners is not None:
          self.maintenance_owners = maintenance_owners
        if config is not None:
          self.config = config
        if role_config_group_ref is not None:
          self.role_config_group_ref = role_config_group_ref
        if zoo_keeper_server_mode is not None:
          self.zoo_keeper_server_mode = zoo_keeper_server_mode
        if entity_status is not None:
          self.entity_status = entity_status

    @property
    def name(self):
        """
        Gets the name of this ApiRole.
        The name of the role. Optional when creating a role since API v6. If not specified, a name will be automatically generated for the role.

        :return: The name of this ApiRole.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApiRole.
        The name of the role. Optional when creating a role since API v6. If not specified, a name will be automatically generated for the role.

        :param name: The name of this ApiRole.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this ApiRole.
        The type of the role, e.g. NAMENODE, DATANODE, TASKTRACKER.

        :return: The type of this ApiRole.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ApiRole.
        The type of the role, e.g. NAMENODE, DATANODE, TASKTRACKER.

        :param type: The type of this ApiRole.
        :type: str
        """

        self._type = type

    @property
    def host_ref(self):
        """
        Gets the host_ref of this ApiRole.
        A reference to the host where this role runs.

        :return: The host_ref of this ApiRole.
        :rtype: ApiHostRef
        """
        return self._host_ref

    @host_ref.setter
    def host_ref(self, host_ref):
        """
        Sets the host_ref of this ApiRole.
        A reference to the host where this role runs.

        :param host_ref: The host_ref of this ApiRole.
        :type: ApiHostRef
        """

        self._host_ref = host_ref

    @property
    def service_ref(self):
        """
        Gets the service_ref of this ApiRole.
        Readonly. A reference to the parent service.

        :return: The service_ref of this ApiRole.
        :rtype: ApiServiceRef
        """
        return self._service_ref

    @service_ref.setter
    def service_ref(self, service_ref):
        """
        Sets the service_ref of this ApiRole.
        Readonly. A reference to the parent service.

        :param service_ref: The service_ref of this ApiRole.
        :type: ApiServiceRef
        """

        self._service_ref = service_ref

    @property
    def role_state(self):
        """
        Gets the role_state of this ApiRole.
        Readonly. The configured run state of this role. Whether it's running, etc.

        :return: The role_state of this ApiRole.
        :rtype: ApiRoleState
        """
        return self._role_state

    @role_state.setter
    def role_state(self, role_state):
        """
        Sets the role_state of this ApiRole.
        Readonly. The configured run state of this role. Whether it's running, etc.

        :param role_state: The role_state of this ApiRole.
        :type: ApiRoleState
        """

        self._role_state = role_state

    @property
    def commission_state(self):
        """
        Gets the commission_state of this ApiRole.
        Readonly. The commission state of this role. Available since API v2.

        :return: The commission_state of this ApiRole.
        :rtype: ApiCommissionState
        """
        return self._commission_state

    @commission_state.setter
    def commission_state(self, commission_state):
        """
        Sets the commission_state of this ApiRole.
        Readonly. The commission state of this role. Available since API v2.

        :param commission_state: The commission_state of this ApiRole.
        :type: ApiCommissionState
        """

        self._commission_state = commission_state

    @property
    def health_summary(self):
        """
        Gets the health_summary of this ApiRole.
        Readonly. The high-level health status of this role.

        :return: The health_summary of this ApiRole.
        :rtype: ApiHealthSummary
        """
        return self._health_summary

    @health_summary.setter
    def health_summary(self, health_summary):
        """
        Sets the health_summary of this ApiRole.
        Readonly. The high-level health status of this role.

        :param health_summary: The health_summary of this ApiRole.
        :type: ApiHealthSummary
        """

        self._health_summary = health_summary

    @property
    def config_stale(self):
        """
        Gets the config_stale of this ApiRole.
        Readonly. Expresses whether the role configuration is stale.

        :return: The config_stale of this ApiRole.
        :rtype: bool
        """
        return self._config_stale

    @config_stale.setter
    def config_stale(self, config_stale):
        """
        Sets the config_stale of this ApiRole.
        Readonly. Expresses whether the role configuration is stale.

        :param config_stale: The config_stale of this ApiRole.
        :type: bool
        """

        self._config_stale = config_stale

    @property
    def config_staleness_status(self):
        """
        Gets the config_staleness_status of this ApiRole.
        Readonly. Expresses the role's configuration staleness status. Available since API v6.

        :return: The config_staleness_status of this ApiRole.
        :rtype: ApiConfigStalenessStatus
        """
        return self._config_staleness_status

    @config_staleness_status.setter
    def config_staleness_status(self, config_staleness_status):
        """
        Sets the config_staleness_status of this ApiRole.
        Readonly. Expresses the role's configuration staleness status. Available since API v6.

        :param config_staleness_status: The config_staleness_status of this ApiRole.
        :type: ApiConfigStalenessStatus
        """

        self._config_staleness_status = config_staleness_status

    @property
    def health_checks(self):
        """
        Gets the health_checks of this ApiRole.
        Readonly. The list of health checks of this service.

        :return: The health_checks of this ApiRole.
        :rtype: list[ApiHealthCheck]
        """
        return self._health_checks

    @health_checks.setter
    def health_checks(self, health_checks):
        """
        Sets the health_checks of this ApiRole.
        Readonly. The list of health checks of this service.

        :param health_checks: The health_checks of this ApiRole.
        :type: list[ApiHealthCheck]
        """

        self._health_checks = health_checks

    @property
    def ha_status(self):
        """
        Gets the ha_status of this ApiRole.
        Readonly. The HA status of this role.

        :return: The ha_status of this ApiRole.
        :rtype: HaStatus
        """
        return self._ha_status

    @ha_status.setter
    def ha_status(self, ha_status):
        """
        Sets the ha_status of this ApiRole.
        Readonly. The HA status of this role.

        :param ha_status: The ha_status of this ApiRole.
        :type: HaStatus
        """

        self._ha_status = ha_status

    @property
    def role_url(self):
        """
        Gets the role_url of this ApiRole.
        Readonly. Link into the Cloudera Manager web UI for this specific role.

        :return: The role_url of this ApiRole.
        :rtype: str
        """
        return self._role_url

    @role_url.setter
    def role_url(self, role_url):
        """
        Sets the role_url of this ApiRole.
        Readonly. Link into the Cloudera Manager web UI for this specific role.

        :param role_url: The role_url of this ApiRole.
        :type: str
        """

        self._role_url = role_url

    @property
    def maintenance_mode(self):
        """
        Gets the maintenance_mode of this ApiRole.
        Readonly. Whether the role is in maintenance mode. Available since API v2.

        :return: The maintenance_mode of this ApiRole.
        :rtype: bool
        """
        return self._maintenance_mode

    @maintenance_mode.setter
    def maintenance_mode(self, maintenance_mode):
        """
        Sets the maintenance_mode of this ApiRole.
        Readonly. Whether the role is in maintenance mode. Available since API v2.

        :param maintenance_mode: The maintenance_mode of this ApiRole.
        :type: bool
        """

        self._maintenance_mode = maintenance_mode

    @property
    def maintenance_owners(self):
        """
        Gets the maintenance_owners of this ApiRole.
        Readonly. The list of objects that trigger this role to be in maintenance mode. Available since API v2.

        :return: The maintenance_owners of this ApiRole.
        :rtype: list[ApiEntityType]
        """
        return self._maintenance_owners

    @maintenance_owners.setter
    def maintenance_owners(self, maintenance_owners):
        """
        Sets the maintenance_owners of this ApiRole.
        Readonly. The list of objects that trigger this role to be in maintenance mode. Available since API v2.

        :param maintenance_owners: The maintenance_owners of this ApiRole.
        :type: list[ApiEntityType]
        """

        self._maintenance_owners = maintenance_owners

    @property
    def config(self):
        """
        Gets the config of this ApiRole.
        The role configuration. Optional.

        :return: The config of this ApiRole.
        :rtype: ApiConfigList
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this ApiRole.
        The role configuration. Optional.

        :param config: The config of this ApiRole.
        :type: ApiConfigList
        """

        self._config = config

    @property
    def role_config_group_ref(self):
        """
        Gets the role_config_group_ref of this ApiRole.
        Readonly. The reference to the role configuration group of this role. Available since API v3.

        :return: The role_config_group_ref of this ApiRole.
        :rtype: ApiRoleConfigGroupRef
        """
        return self._role_config_group_ref

    @role_config_group_ref.setter
    def role_config_group_ref(self, role_config_group_ref):
        """
        Sets the role_config_group_ref of this ApiRole.
        Readonly. The reference to the role configuration group of this role. Available since API v3.

        :param role_config_group_ref: The role_config_group_ref of this ApiRole.
        :type: ApiRoleConfigGroupRef
        """

        self._role_config_group_ref = role_config_group_ref

    @property
    def zoo_keeper_server_mode(self):
        """
        Gets the zoo_keeper_server_mode of this ApiRole.
        Readonly. The ZooKeeper server mode for this role. Note that for non-ZooKeeper Server roles this will be null. Available since API v6.

        :return: The zoo_keeper_server_mode of this ApiRole.
        :rtype: ZooKeeperServerMode
        """
        return self._zoo_keeper_server_mode

    @zoo_keeper_server_mode.setter
    def zoo_keeper_server_mode(self, zoo_keeper_server_mode):
        """
        Sets the zoo_keeper_server_mode of this ApiRole.
        Readonly. The ZooKeeper server mode for this role. Note that for non-ZooKeeper Server roles this will be null. Available since API v6.

        :param zoo_keeper_server_mode: The zoo_keeper_server_mode of this ApiRole.
        :type: ZooKeeperServerMode
        """

        self._zoo_keeper_server_mode = zoo_keeper_server_mode

    @property
    def entity_status(self):
        """
        Gets the entity_status of this ApiRole.
        Readonly. The entity status for this role. Available since API v11.

        :return: The entity_status of this ApiRole.
        :rtype: ApiEntityStatus
        """
        return self._entity_status

    @entity_status.setter
    def entity_status(self, entity_status):
        """
        Sets the entity_status of this ApiRole.
        Readonly. The entity status for this role. Available since API v11.

        :param entity_status: The entity_status of this ApiRole.
        :type: ApiEntityStatus
        """

        self._entity_status = entity_status

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
        if not isinstance(other, ApiRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class ApiReplicationCommand(object):
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
        'id': 'float',
        'name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'active': 'bool',
        'success': 'bool',
        'result_message': 'str',
        'result_data_url': 'str',
        'cluster_ref': 'ApiClusterRef',
        'service_ref': 'ApiServiceRef',
        'role_ref': 'ApiRoleRef',
        'host_ref': 'ApiHostRef',
        'parent': 'ApiCommand',
        'children': 'ApiCommandList',
        'can_retry': 'bool',
        'hdfs_result': 'ApiHdfsReplicationResult',
        'hive_result': 'ApiHiveReplicationResult'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'active': 'active',
        'success': 'success',
        'result_message': 'resultMessage',
        'result_data_url': 'resultDataUrl',
        'cluster_ref': 'clusterRef',
        'service_ref': 'serviceRef',
        'role_ref': 'roleRef',
        'host_ref': 'hostRef',
        'parent': 'parent',
        'children': 'children',
        'can_retry': 'canRetry',
        'hdfs_result': 'hdfsResult',
        'hive_result': 'hiveResult'
    }

    def __init__(self, id=None, name=None, start_time=None, end_time=None, active=None, success=None, result_message=None, result_data_url=None, cluster_ref=None, service_ref=None, role_ref=None, host_ref=None, parent=None, children=None, can_retry=None, hdfs_result=None, hive_result=None):
        """
        ApiReplicationCommand - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._start_time = None
        self._end_time = None
        self._active = None
        self._success = None
        self._result_message = None
        self._result_data_url = None
        self._cluster_ref = None
        self._service_ref = None
        self._role_ref = None
        self._host_ref = None
        self._parent = None
        self._children = None
        self._can_retry = None
        self._hdfs_result = None
        self._hive_result = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if active is not None:
          self.active = active
        if success is not None:
          self.success = success
        if result_message is not None:
          self.result_message = result_message
        if result_data_url is not None:
          self.result_data_url = result_data_url
        if cluster_ref is not None:
          self.cluster_ref = cluster_ref
        if service_ref is not None:
          self.service_ref = service_ref
        if role_ref is not None:
          self.role_ref = role_ref
        if host_ref is not None:
          self.host_ref = host_ref
        if parent is not None:
          self.parent = parent
        if children is not None:
          self.children = children
        if can_retry is not None:
          self.can_retry = can_retry
        if hdfs_result is not None:
          self.hdfs_result = hdfs_result
        if hive_result is not None:
          self.hive_result = hive_result

    @property
    def id(self):
        """
        Gets the id of this ApiReplicationCommand.
        The command ID.

        :return: The id of this ApiReplicationCommand.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApiReplicationCommand.
        The command ID.

        :param id: The id of this ApiReplicationCommand.
        :type: float
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ApiReplicationCommand.
        The command name.

        :return: The name of this ApiReplicationCommand.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ApiReplicationCommand.
        The command name.

        :param name: The name of this ApiReplicationCommand.
        :type: str
        """

        self._name = name

    @property
    def start_time(self):
        """
        Gets the start_time of this ApiReplicationCommand.
        The start time.

        :return: The start_time of this ApiReplicationCommand.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this ApiReplicationCommand.
        The start time.

        :param start_time: The start_time of this ApiReplicationCommand.
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this ApiReplicationCommand.
        The end time, if the command is finished.

        :return: The end_time of this ApiReplicationCommand.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this ApiReplicationCommand.
        The end time, if the command is finished.

        :param end_time: The end_time of this ApiReplicationCommand.
        :type: str
        """

        self._end_time = end_time

    @property
    def active(self):
        """
        Gets the active of this ApiReplicationCommand.
        Whether the command is currently active.

        :return: The active of this ApiReplicationCommand.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ApiReplicationCommand.
        Whether the command is currently active.

        :param active: The active of this ApiReplicationCommand.
        :type: bool
        """

        self._active = active

    @property
    def success(self):
        """
        Gets the success of this ApiReplicationCommand.
        If the command is finished, whether it was successful.

        :return: The success of this ApiReplicationCommand.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """
        Sets the success of this ApiReplicationCommand.
        If the command is finished, whether it was successful.

        :param success: The success of this ApiReplicationCommand.
        :type: bool
        """

        self._success = success

    @property
    def result_message(self):
        """
        Gets the result_message of this ApiReplicationCommand.
        If the command is finished, the result message.

        :return: The result_message of this ApiReplicationCommand.
        :rtype: str
        """
        return self._result_message

    @result_message.setter
    def result_message(self, result_message):
        """
        Sets the result_message of this ApiReplicationCommand.
        If the command is finished, the result message.

        :param result_message: The result_message of this ApiReplicationCommand.
        :type: str
        """

        self._result_message = result_message

    @property
    def result_data_url(self):
        """
        Gets the result_data_url of this ApiReplicationCommand.
        URL to the command's downloadable result data, if any exists.

        :return: The result_data_url of this ApiReplicationCommand.
        :rtype: str
        """
        return self._result_data_url

    @result_data_url.setter
    def result_data_url(self, result_data_url):
        """
        Sets the result_data_url of this ApiReplicationCommand.
        URL to the command's downloadable result data, if any exists.

        :param result_data_url: The result_data_url of this ApiReplicationCommand.
        :type: str
        """

        self._result_data_url = result_data_url

    @property
    def cluster_ref(self):
        """
        Gets the cluster_ref of this ApiReplicationCommand.
        Reference to the cluster (for cluster commands only).

        :return: The cluster_ref of this ApiReplicationCommand.
        :rtype: ApiClusterRef
        """
        return self._cluster_ref

    @cluster_ref.setter
    def cluster_ref(self, cluster_ref):
        """
        Sets the cluster_ref of this ApiReplicationCommand.
        Reference to the cluster (for cluster commands only).

        :param cluster_ref: The cluster_ref of this ApiReplicationCommand.
        :type: ApiClusterRef
        """

        self._cluster_ref = cluster_ref

    @property
    def service_ref(self):
        """
        Gets the service_ref of this ApiReplicationCommand.
        Reference to the service (for service commands only).

        :return: The service_ref of this ApiReplicationCommand.
        :rtype: ApiServiceRef
        """
        return self._service_ref

    @service_ref.setter
    def service_ref(self, service_ref):
        """
        Sets the service_ref of this ApiReplicationCommand.
        Reference to the service (for service commands only).

        :param service_ref: The service_ref of this ApiReplicationCommand.
        :type: ApiServiceRef
        """

        self._service_ref = service_ref

    @property
    def role_ref(self):
        """
        Gets the role_ref of this ApiReplicationCommand.
        Reference to the role (for role commands only).

        :return: The role_ref of this ApiReplicationCommand.
        :rtype: ApiRoleRef
        """
        return self._role_ref

    @role_ref.setter
    def role_ref(self, role_ref):
        """
        Sets the role_ref of this ApiReplicationCommand.
        Reference to the role (for role commands only).

        :param role_ref: The role_ref of this ApiReplicationCommand.
        :type: ApiRoleRef
        """

        self._role_ref = role_ref

    @property
    def host_ref(self):
        """
        Gets the host_ref of this ApiReplicationCommand.
        Reference to the host (for host commands only).

        :return: The host_ref of this ApiReplicationCommand.
        :rtype: ApiHostRef
        """
        return self._host_ref

    @host_ref.setter
    def host_ref(self, host_ref):
        """
        Sets the host_ref of this ApiReplicationCommand.
        Reference to the host (for host commands only).

        :param host_ref: The host_ref of this ApiReplicationCommand.
        :type: ApiHostRef
        """

        self._host_ref = host_ref

    @property
    def parent(self):
        """
        Gets the parent of this ApiReplicationCommand.
        Reference to the parent command, if any.

        :return: The parent of this ApiReplicationCommand.
        :rtype: ApiCommand
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this ApiReplicationCommand.
        Reference to the parent command, if any.

        :param parent: The parent of this ApiReplicationCommand.
        :type: ApiCommand
        """

        self._parent = parent

    @property
    def children(self):
        """
        Gets the children of this ApiReplicationCommand.
        List of child commands. Only available in the full view. <p> The list contains only the summary view of the children.

        :return: The children of this ApiReplicationCommand.
        :rtype: ApiCommandList
        """
        return self._children

    @children.setter
    def children(self, children):
        """
        Sets the children of this ApiReplicationCommand.
        List of child commands. Only available in the full view. <p> The list contains only the summary view of the children.

        :param children: The children of this ApiReplicationCommand.
        :type: ApiCommandList
        """

        self._children = children

    @property
    def can_retry(self):
        """
        Gets the can_retry of this ApiReplicationCommand.
        If the command can be retried. Available since V11

        :return: The can_retry of this ApiReplicationCommand.
        :rtype: bool
        """
        return self._can_retry

    @can_retry.setter
    def can_retry(self, can_retry):
        """
        Sets the can_retry of this ApiReplicationCommand.
        If the command can be retried. Available since V11

        :param can_retry: The can_retry of this ApiReplicationCommand.
        :type: bool
        """

        self._can_retry = can_retry

    @property
    def hdfs_result(self):
        """
        Gets the hdfs_result of this ApiReplicationCommand.
        Results for replication commands on HDFS services.

        :return: The hdfs_result of this ApiReplicationCommand.
        :rtype: ApiHdfsReplicationResult
        """
        return self._hdfs_result

    @hdfs_result.setter
    def hdfs_result(self, hdfs_result):
        """
        Sets the hdfs_result of this ApiReplicationCommand.
        Results for replication commands on HDFS services.

        :param hdfs_result: The hdfs_result of this ApiReplicationCommand.
        :type: ApiHdfsReplicationResult
        """

        self._hdfs_result = hdfs_result

    @property
    def hive_result(self):
        """
        Gets the hive_result of this ApiReplicationCommand.
        Results for replication commands on Hive services.

        :return: The hive_result of this ApiReplicationCommand.
        :rtype: ApiHiveReplicationResult
        """
        return self._hive_result

    @hive_result.setter
    def hive_result(self, hive_result):
        """
        Sets the hive_result of this ApiReplicationCommand.
        Results for replication commands on Hive services.

        :param hive_result: The hive_result of this ApiReplicationCommand.
        :type: ApiHiveReplicationResult
        """

        self._hive_result = hive_result

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
        if not isinstance(other, ApiReplicationCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

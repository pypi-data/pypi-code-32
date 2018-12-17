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


class ApiHdfsSnapshot(object):
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
        'path': 'str',
        'snapshot_name': 'str',
        'snapshot_path': 'str',
        'creation_time': 'str'
    }

    attribute_map = {
        'path': 'path',
        'snapshot_name': 'snapshotName',
        'snapshot_path': 'snapshotPath',
        'creation_time': 'creationTime'
    }

    def __init__(self, path=None, snapshot_name=None, snapshot_path=None, creation_time=None):
        """
        ApiHdfsSnapshot - a model defined in Swagger
        """

        self._path = None
        self._snapshot_name = None
        self._snapshot_path = None
        self._creation_time = None

        if path is not None:
          self.path = path
        if snapshot_name is not None:
          self.snapshot_name = snapshot_name
        if snapshot_path is not None:
          self.snapshot_path = snapshot_path
        if creation_time is not None:
          self.creation_time = creation_time

    @property
    def path(self):
        """
        Gets the path of this ApiHdfsSnapshot.
        Snapshotted path.

        :return: The path of this ApiHdfsSnapshot.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ApiHdfsSnapshot.
        Snapshotted path.

        :param path: The path of this ApiHdfsSnapshot.
        :type: str
        """

        self._path = path

    @property
    def snapshot_name(self):
        """
        Gets the snapshot_name of this ApiHdfsSnapshot.
        Snapshot name.

        :return: The snapshot_name of this ApiHdfsSnapshot.
        :rtype: str
        """
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, snapshot_name):
        """
        Sets the snapshot_name of this ApiHdfsSnapshot.
        Snapshot name.

        :param snapshot_name: The snapshot_name of this ApiHdfsSnapshot.
        :type: str
        """

        self._snapshot_name = snapshot_name

    @property
    def snapshot_path(self):
        """
        Gets the snapshot_path of this ApiHdfsSnapshot.
        Read-only. Fully qualified path for the snapshot version of \"path\". <p/> For example, if a snapshot \"s1\" is present at \"/a/.snapshot/s1, then the snapshot path corresponding to \"s1\" for path \"/a/b\" will be \"/a/.snapshot/s1/b\".

        :return: The snapshot_path of this ApiHdfsSnapshot.
        :rtype: str
        """
        return self._snapshot_path

    @snapshot_path.setter
    def snapshot_path(self, snapshot_path):
        """
        Sets the snapshot_path of this ApiHdfsSnapshot.
        Read-only. Fully qualified path for the snapshot version of \"path\". <p/> For example, if a snapshot \"s1\" is present at \"/a/.snapshot/s1, then the snapshot path corresponding to \"s1\" for path \"/a/b\" will be \"/a/.snapshot/s1/b\".

        :param snapshot_path: The snapshot_path of this ApiHdfsSnapshot.
        :type: str
        """

        self._snapshot_path = snapshot_path

    @property
    def creation_time(self):
        """
        Gets the creation_time of this ApiHdfsSnapshot.
        Snapshot creation time.

        :return: The creation_time of this ApiHdfsSnapshot.
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this ApiHdfsSnapshot.
        Snapshot creation time.

        :param creation_time: The creation_time of this ApiHdfsSnapshot.
        :type: str
        """

        self._creation_time = creation_time

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
        if not isinstance(other, ApiHdfsSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

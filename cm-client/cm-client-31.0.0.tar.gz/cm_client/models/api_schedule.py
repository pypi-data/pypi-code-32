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


class ApiSchedule(object):
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
        'display_name': 'str',
        'description': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'interval': 'float',
        'interval_unit': 'ApiScheduleInterval',
        'next_run': 'str',
        'paused': 'bool',
        'alert_on_start': 'bool',
        'alert_on_success': 'bool',
        'alert_on_fail': 'bool',
        'alert_on_abort': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'interval': 'interval',
        'interval_unit': 'intervalUnit',
        'next_run': 'nextRun',
        'paused': 'paused',
        'alert_on_start': 'alertOnStart',
        'alert_on_success': 'alertOnSuccess',
        'alert_on_fail': 'alertOnFail',
        'alert_on_abort': 'alertOnAbort'
    }

    def __init__(self, id=None, display_name=None, description=None, start_time=None, end_time=None, interval=None, interval_unit=None, next_run=None, paused=None, alert_on_start=None, alert_on_success=None, alert_on_fail=None, alert_on_abort=None):
        """
        ApiSchedule - a model defined in Swagger
        """

        self._id = None
        self._display_name = None
        self._description = None
        self._start_time = None
        self._end_time = None
        self._interval = None
        self._interval_unit = None
        self._next_run = None
        self._paused = None
        self._alert_on_start = None
        self._alert_on_success = None
        self._alert_on_fail = None
        self._alert_on_abort = None

        if id is not None:
          self.id = id
        if display_name is not None:
          self.display_name = display_name
        if description is not None:
          self.description = description
        if start_time is not None:
          self.start_time = start_time
        if end_time is not None:
          self.end_time = end_time
        if interval is not None:
          self.interval = interval
        if interval_unit is not None:
          self.interval_unit = interval_unit
        if next_run is not None:
          self.next_run = next_run
        if paused is not None:
          self.paused = paused
        if alert_on_start is not None:
          self.alert_on_start = alert_on_start
        if alert_on_success is not None:
          self.alert_on_success = alert_on_success
        if alert_on_fail is not None:
          self.alert_on_fail = alert_on_fail
        if alert_on_abort is not None:
          self.alert_on_abort = alert_on_abort

    @property
    def id(self):
        """
        Gets the id of this ApiSchedule.
        The schedule id.

        :return: The id of this ApiSchedule.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ApiSchedule.
        The schedule id.

        :param id: The id of this ApiSchedule.
        :type: float
        """

        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this ApiSchedule.
        The schedule display name.

        :return: The display_name of this ApiSchedule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ApiSchedule.
        The schedule display name.

        :param display_name: The display_name of this ApiSchedule.
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ApiSchedule.
        The schedule description.

        :return: The description of this ApiSchedule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ApiSchedule.
        The schedule description.

        :param description: The description of this ApiSchedule.
        :type: str
        """

        self._description = description

    @property
    def start_time(self):
        """
        Gets the start_time of this ApiSchedule.
        The time at which the scheduled activity is triggered for the first time.

        :return: The start_time of this ApiSchedule.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this ApiSchedule.
        The time at which the scheduled activity is triggered for the first time.

        :param start_time: The start_time of this ApiSchedule.
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this ApiSchedule.
        The time after which the scheduled activity will no longer be triggered.

        :return: The end_time of this ApiSchedule.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this ApiSchedule.
        The time after which the scheduled activity will no longer be triggered.

        :param end_time: The end_time of this ApiSchedule.
        :type: str
        """

        self._end_time = end_time

    @property
    def interval(self):
        """
        Gets the interval of this ApiSchedule.
        The duration between consecutive triggers of a scheduled activity.

        :return: The interval of this ApiSchedule.
        :rtype: float
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this ApiSchedule.
        The duration between consecutive triggers of a scheduled activity.

        :param interval: The interval of this ApiSchedule.
        :type: float
        """

        self._interval = interval

    @property
    def interval_unit(self):
        """
        Gets the interval_unit of this ApiSchedule.
        The unit for the repeat interval.

        :return: The interval_unit of this ApiSchedule.
        :rtype: ApiScheduleInterval
        """
        return self._interval_unit

    @interval_unit.setter
    def interval_unit(self, interval_unit):
        """
        Sets the interval_unit of this ApiSchedule.
        The unit for the repeat interval.

        :param interval_unit: The interval_unit of this ApiSchedule.
        :type: ApiScheduleInterval
        """

        self._interval_unit = interval_unit

    @property
    def next_run(self):
        """
        Gets the next_run of this ApiSchedule.
        Readonly. The time the scheduled command will run next.

        :return: The next_run of this ApiSchedule.
        :rtype: str
        """
        return self._next_run

    @next_run.setter
    def next_run(self, next_run):
        """
        Sets the next_run of this ApiSchedule.
        Readonly. The time the scheduled command will run next.

        :param next_run: The next_run of this ApiSchedule.
        :type: str
        """

        self._next_run = next_run

    @property
    def paused(self):
        """
        Gets the paused of this ApiSchedule.
        The paused state for the schedule. The scheduled activity will not be triggered as long as the scheduled is paused.

        :return: The paused of this ApiSchedule.
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """
        Sets the paused of this ApiSchedule.
        The paused state for the schedule. The scheduled activity will not be triggered as long as the scheduled is paused.

        :param paused: The paused of this ApiSchedule.
        :type: bool
        """

        self._paused = paused

    @property
    def alert_on_start(self):
        """
        Gets the alert_on_start of this ApiSchedule.
        Whether to alert on start of the scheduled activity.

        :return: The alert_on_start of this ApiSchedule.
        :rtype: bool
        """
        return self._alert_on_start

    @alert_on_start.setter
    def alert_on_start(self, alert_on_start):
        """
        Sets the alert_on_start of this ApiSchedule.
        Whether to alert on start of the scheduled activity.

        :param alert_on_start: The alert_on_start of this ApiSchedule.
        :type: bool
        """

        self._alert_on_start = alert_on_start

    @property
    def alert_on_success(self):
        """
        Gets the alert_on_success of this ApiSchedule.
        Whether to alert on successful completion of the scheduled activity.

        :return: The alert_on_success of this ApiSchedule.
        :rtype: bool
        """
        return self._alert_on_success

    @alert_on_success.setter
    def alert_on_success(self, alert_on_success):
        """
        Sets the alert_on_success of this ApiSchedule.
        Whether to alert on successful completion of the scheduled activity.

        :param alert_on_success: The alert_on_success of this ApiSchedule.
        :type: bool
        """

        self._alert_on_success = alert_on_success

    @property
    def alert_on_fail(self):
        """
        Gets the alert_on_fail of this ApiSchedule.
        Whether to alert on failure of the scheduled activity.

        :return: The alert_on_fail of this ApiSchedule.
        :rtype: bool
        """
        return self._alert_on_fail

    @alert_on_fail.setter
    def alert_on_fail(self, alert_on_fail):
        """
        Sets the alert_on_fail of this ApiSchedule.
        Whether to alert on failure of the scheduled activity.

        :param alert_on_fail: The alert_on_fail of this ApiSchedule.
        :type: bool
        """

        self._alert_on_fail = alert_on_fail

    @property
    def alert_on_abort(self):
        """
        Gets the alert_on_abort of this ApiSchedule.
        Whether to alert on abort of the scheduled activity.

        :return: The alert_on_abort of this ApiSchedule.
        :rtype: bool
        """
        return self._alert_on_abort

    @alert_on_abort.setter
    def alert_on_abort(self, alert_on_abort):
        """
        Sets the alert_on_abort of this ApiSchedule.
        Whether to alert on abort of the scheduled activity.

        :param alert_on_abort: The alert_on_abort of this ApiSchedule.
        :type: bool
        """

        self._alert_on_abort = alert_on_abort

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
        if not isinstance(other, ApiSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountRateChild(Model):
    """AccountRateChild.

    :param rate:
    :type rate: ~energycap.sdk.models.RateChild
    :param start_date:
    :type start_date: datetime
    :param end_date:
    :type end_date: datetime
    """

    _attribute_map = {
        'rate': {'key': 'rate', 'type': 'RateChild'},
        'start_date': {'key': 'startDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
    }

    def __init__(self, rate=None, start_date=None, end_date=None):
        super(AccountRateChild, self).__init__()
        self.rate = rate
        self.start_date = start_date
        self.end_date = end_date

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportGroupResponse(Model):
    """ReportGroupResponse.

    :param report_group_id:
    :type report_group_id: int
    :param report_group_code:
    :type report_group_code: str
    :param report_group_info:
    :type report_group_info: str
    :param reports:
    :type reports: list[~energycap.sdk.models.ReportChild]
    """

    _attribute_map = {
        'report_group_id': {'key': 'reportGroupId', 'type': 'int'},
        'report_group_code': {'key': 'reportGroupCode', 'type': 'str'},
        'report_group_info': {'key': 'reportGroupInfo', 'type': 'str'},
        'reports': {'key': 'reports', 'type': '[ReportChild]'},
    }

    def __init__(self, report_group_id=None, report_group_code=None, report_group_info=None, reports=None):
        super(ReportGroupResponse, self).__init__()
        self.report_group_id = report_group_id
        self.report_group_code = report_group_code
        self.report_group_info = report_group_info
        self.reports = reports

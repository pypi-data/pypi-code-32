# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SpecificAuditResponse(Model):
    """SpecificAuditResponse.

    :param audit_category:
    :type audit_category: ~energycap.sdk.models.AuditCategory
    :param alert_severity:
    :type alert_severity: ~energycap.sdk.models.AlertSeverityResponse
    :param skip_zero_comparison:
    :type skip_zero_comparison: bool
    :param properties:
    :type properties: list[~energycap.sdk.models.AuditProperty]
    :param specific_audit_id:
    :type specific_audit_id: int
    :param specific_audit_info:
    :type specific_audit_info: str
    :param auditor_id:
    :type auditor_id: int
    :param auditor_code:
    :type auditor_code: str
    :param description:
    :type description: str
    """

    _attribute_map = {
        'audit_category': {'key': 'auditCategory', 'type': 'AuditCategory'},
        'alert_severity': {'key': 'alertSeverity', 'type': 'AlertSeverityResponse'},
        'skip_zero_comparison': {'key': 'skipZeroComparison', 'type': 'bool'},
        'properties': {'key': 'properties', 'type': '[AuditProperty]'},
        'specific_audit_id': {'key': 'specificAuditId', 'type': 'int'},
        'specific_audit_info': {'key': 'specificAuditInfo', 'type': 'str'},
        'auditor_id': {'key': 'auditorId', 'type': 'int'},
        'auditor_code': {'key': 'auditorCode', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, audit_category=None, alert_severity=None, skip_zero_comparison=None, properties=None, specific_audit_id=None, specific_audit_info=None, auditor_id=None, auditor_code=None, description=None):
        super(SpecificAuditResponse, self).__init__()
        self.audit_category = audit_category
        self.alert_severity = alert_severity
        self.skip_zero_comparison = skip_zero_comparison
        self.properties = properties
        self.specific_audit_id = specific_audit_id
        self.specific_audit_info = specific_audit_info
        self.auditor_id = auditor_id
        self.auditor_code = auditor_code
        self.description = description

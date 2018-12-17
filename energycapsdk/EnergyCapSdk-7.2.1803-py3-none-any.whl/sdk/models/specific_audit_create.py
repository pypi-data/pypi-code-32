# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SpecificAuditCreate(Model):
    """SpecificAuditCreate.

    :param specific_audit_info: Name used to refer to this audit <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 64 characters</span>
    :type specific_audit_info: str
    :param auditor_id: The Id of the bill audit to add to the group <span
     class='property-internal'>Required</span>
    :type auditor_id: int
    """

    _validation = {
        'specific_audit_info': {'required': True, 'max_length': 64, 'min_length': 0},
        'auditor_id': {'required': True},
    }

    _attribute_map = {
        'specific_audit_info': {'key': 'specificAuditInfo', 'type': 'str'},
        'auditor_id': {'key': 'auditorId', 'type': 'int'},
    }

    def __init__(self, specific_audit_info, auditor_id):
        super(SpecificAuditCreate, self).__init__()
        self.specific_audit_info = specific_audit_info
        self.auditor_id = auditor_id

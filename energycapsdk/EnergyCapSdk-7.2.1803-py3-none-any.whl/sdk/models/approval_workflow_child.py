# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApprovalWorkflowChild(Model):
    """ApprovalWorkflowChild.

    :param approval_mode_enabled:
    :type approval_mode_enabled: bool
    :param confirm_edit_delete:
    :type confirm_edit_delete: bool
    """

    _attribute_map = {
        'approval_mode_enabled': {'key': 'approvalModeEnabled', 'type': 'bool'},
        'confirm_edit_delete': {'key': 'confirmEditDelete', 'type': 'bool'},
    }

    def __init__(self, approval_mode_enabled=None, confirm_edit_delete=None):
        super(ApprovalWorkflowChild, self).__init__()
        self.approval_mode_enabled = approval_mode_enabled
        self.confirm_edit_delete = confirm_edit_delete

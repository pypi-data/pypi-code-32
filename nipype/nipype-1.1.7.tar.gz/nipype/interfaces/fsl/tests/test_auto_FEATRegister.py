# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import FEATRegister


def test_FEATRegister_inputs():
    input_map = dict(
        feat_dirs=dict(mandatory=True, ),
        reg_dof=dict(usedefault=True, ),
        reg_image=dict(mandatory=True, ),
    )
    inputs = FEATRegister.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FEATRegister_outputs():
    output_map = dict(fsf_file=dict(), )
    outputs = FEATRegister.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

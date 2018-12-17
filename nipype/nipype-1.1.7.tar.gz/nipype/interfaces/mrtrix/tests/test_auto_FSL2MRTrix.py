# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..tensors import FSL2MRTrix


def test_FSL2MRTrix_inputs():
    input_map = dict(
        bval_file=dict(mandatory=True, ),
        bvec_file=dict(mandatory=True, ),
        invert_x=dict(usedefault=True, ),
        invert_y=dict(usedefault=True, ),
        invert_z=dict(usedefault=True, ),
        out_encoding_file=dict(genfile=True, ),
    )
    inputs = FSL2MRTrix.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FSL2MRTrix_outputs():
    output_map = dict(encoding_file=dict(), )
    outputs = FSL2MRTrix.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..dcmstack import SplitNifti


def test_SplitNifti_inputs():
    input_map = dict(
        in_file=dict(mandatory=True, ),
        out_ext=dict(usedefault=True, ),
        out_format=dict(),
        out_path=dict(),
        split_dim=dict(),
    )
    inputs = SplitNifti.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SplitNifti_outputs():
    output_map = dict(out_list=dict(), )
    outputs = SplitNifti.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

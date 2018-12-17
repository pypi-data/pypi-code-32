# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import Analyze2nii


def test_Analyze2nii_inputs():
    input_map = dict(
        analyze_file=dict(mandatory=True, ),
        matlab_cmd=dict(),
        mfile=dict(usedefault=True, ),
        paths=dict(),
        use_mcr=dict(),
        use_v8struct=dict(
            min_ver='8',
            usedefault=True,
        ),
    )
    inputs = Analyze2nii.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Analyze2nii_outputs():
    output_map = dict(
        matlab_cmd=dict(),
        mfile=dict(usedefault=True, ),
        nifti_file=dict(),
        paths=dict(),
        use_mcr=dict(),
        use_v8struct=dict(
            min_ver='8',
            usedefault=True,
        ),
    )
    outputs = Analyze2nii.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

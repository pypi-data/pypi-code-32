# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..arithmetic import CastScalarVolume


def test_CastScalarVolume_inputs():
    input_map = dict(
        InputVolume=dict(
            argstr='%s',
            position=-2,
        ),
        OutputVolume=dict(
            argstr='%s',
            hash_files=False,
            position=-1,
        ),
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        type=dict(argstr='--type %s', ),
    )
    inputs = CastScalarVolume.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_CastScalarVolume_outputs():
    output_map = dict(OutputVolume=dict(position=-1, ), )
    outputs = CastScalarVolume.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

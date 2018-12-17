# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..surface import MergeModels


def test_MergeModels_inputs():
    input_map = dict(
        Model1=dict(
            argstr='%s',
            position=-3,
        ),
        Model2=dict(
            argstr='%s',
            position=-2,
        ),
        ModelOutput=dict(
            argstr='%s',
            hash_files=False,
            position=-1,
        ),
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
    )
    inputs = MergeModels.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MergeModels_outputs():
    output_map = dict(ModelOutput=dict(position=-1, ), )
    outputs = MergeModels.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

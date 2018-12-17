# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import GCOR


def test_GCOR_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-input %s',
            copyfile=False,
            mandatory=True,
            position=-1,
        ),
        mask=dict(
            argstr='-mask %s',
            copyfile=False,
        ),
        nfirst=dict(argstr='-nfirst %d', ),
        no_demean=dict(argstr='-no_demean', ),
    )
    inputs = GCOR.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_GCOR_outputs():
    output_map = dict(out=dict(), )
    outputs = GCOR.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import ConcatenateLTA


def test_ConcatenateLTA_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_lta1=dict(
            argstr='%s',
            mandatory=True,
            position=-3,
        ),
        in_lta2=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        invert_1=dict(argstr='-invert1', ),
        invert_2=dict(argstr='-invert2', ),
        invert_out=dict(argstr='-invertout', ),
        out_file=dict(
            argstr='%s',
            hash_files=False,
            keep_extension=True,
            name_source=['in_lta1'],
            name_template='%s_concat',
            position=-1,
        ),
        out_type=dict(argstr='-out_type %d', ),
        subject=dict(argstr='-subject %s', ),
        subjects_dir=dict(),
        tal_source_file=dict(
            argstr='-tal %s',
            position=-5,
            requires=['tal_template_file'],
        ),
        tal_template_file=dict(
            argstr='%s',
            position=-4,
            requires=['tal_source_file'],
        ),
    )
    inputs = ConcatenateLTA.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ConcatenateLTA_outputs():
    output_map = dict(out_file=dict(), )
    outputs = ConcatenateLTA.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

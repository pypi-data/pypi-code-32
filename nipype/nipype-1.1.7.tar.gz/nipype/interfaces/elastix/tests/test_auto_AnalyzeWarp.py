# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..registration import AnalyzeWarp


def test_AnalyzeWarp_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        jac=dict(
            argstr='-jac %s',
            usedefault=True,
        ),
        jacmat=dict(
            argstr='-jacmat %s',
            usedefault=True,
        ),
        moving_image=dict(argstr='-in %s', ),
        num_threads=dict(
            argstr='-threads %01d',
            nohash=True,
            usedefault=True,
        ),
        output_path=dict(
            argstr='-out %s',
            mandatory=True,
            usedefault=True,
        ),
        points=dict(
            argstr='-def %s',
            position=0,
            usedefault=True,
        ),
        transform_file=dict(
            argstr='-tp %s',
            mandatory=True,
        ),
    )
    inputs = AnalyzeWarp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_AnalyzeWarp_outputs():
    output_map = dict(
        disp_field=dict(),
        jacdet_map=dict(),
        jacmat_map=dict(),
    )
    outputs = AnalyzeWarp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

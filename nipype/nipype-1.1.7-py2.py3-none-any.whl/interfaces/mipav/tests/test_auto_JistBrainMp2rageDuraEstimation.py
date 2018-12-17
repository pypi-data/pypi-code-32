# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..developer import JistBrainMp2rageDuraEstimation


def test_JistBrainMp2rageDuraEstimation_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inDistance=dict(argstr='--inDistance %f', ),
        inSecond=dict(argstr='--inSecond %s', ),
        inSkull=dict(argstr='--inSkull %s', ),
        inoutput=dict(argstr='--inoutput %s', ),
        null=dict(argstr='--null %s', ),
        outDura=dict(
            argstr='--outDura %s',
            hash_files=False,
        ),
        xDefaultMem=dict(argstr='-xDefaultMem %d', ),
        xMaxProcess=dict(
            argstr='-xMaxProcess %d',
            usedefault=True,
        ),
        xPrefExt=dict(argstr='--xPrefExt %s', ),
    )
    inputs = JistBrainMp2rageDuraEstimation.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_JistBrainMp2rageDuraEstimation_outputs():
    output_map = dict(outDura=dict(), )
    outputs = JistBrainMp2rageDuraEstimation.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

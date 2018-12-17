# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brains import landmarksConstellationWeights


def test_landmarksConstellationWeights_inputs():
    input_map = dict(
        LLSModel=dict(argstr='--LLSModel %s', ),
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputTemplateModel=dict(argstr='--inputTemplateModel %s', ),
        inputTrainingList=dict(argstr='--inputTrainingList %s', ),
        outputWeightsList=dict(
            argstr='--outputWeightsList %s',
            hash_files=False,
        ),
    )
    inputs = landmarksConstellationWeights.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_landmarksConstellationWeights_outputs():
    output_map = dict(outputWeightsList=dict(), )
    outputs = landmarksConstellationWeights.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

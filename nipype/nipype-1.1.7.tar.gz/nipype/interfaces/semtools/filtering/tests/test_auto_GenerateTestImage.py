# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..featuredetection import GenerateTestImage


def test_GenerateTestImage_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputVolume=dict(argstr='--inputVolume %s', ),
        lowerBoundOfOutputVolume=dict(
            argstr='--lowerBoundOfOutputVolume %f', ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
        outputVolumeSize=dict(argstr='--outputVolumeSize %f', ),
        upperBoundOfOutputVolume=dict(
            argstr='--upperBoundOfOutputVolume %f', ),
    )
    inputs = GenerateTestImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_GenerateTestImage_outputs():
    output_map = dict(outputVolume=dict(), )
    outputs = GenerateTestImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

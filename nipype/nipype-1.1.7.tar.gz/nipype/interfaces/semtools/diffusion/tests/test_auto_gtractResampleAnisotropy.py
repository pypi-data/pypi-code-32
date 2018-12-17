# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..gtract import gtractResampleAnisotropy


def test_gtractResampleAnisotropy_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputAnatomicalVolume=dict(argstr='--inputAnatomicalVolume %s', ),
        inputAnisotropyVolume=dict(argstr='--inputAnisotropyVolume %s', ),
        inputTransform=dict(argstr='--inputTransform %s', ),
        numberOfThreads=dict(argstr='--numberOfThreads %d', ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
        transformType=dict(argstr='--transformType %s', ),
    )
    inputs = gtractResampleAnisotropy.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_gtractResampleAnisotropy_outputs():
    output_map = dict(outputVolume=dict(), )
    outputs = gtractResampleAnisotropy.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

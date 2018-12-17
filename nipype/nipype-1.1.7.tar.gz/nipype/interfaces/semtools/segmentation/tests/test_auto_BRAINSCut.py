# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..specialized import BRAINSCut


def test_BRAINSCut_inputs():
    input_map = dict(
        NoTrainingVectorShuffling=dict(
            argstr='--NoTrainingVectorShuffling ', ),
        applyModel=dict(argstr='--applyModel ', ),
        args=dict(argstr='%s', ),
        computeSSEOn=dict(argstr='--computeSSEOn ', ),
        createVectors=dict(argstr='--createVectors ', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        generateProbability=dict(argstr='--generateProbability ', ),
        histogramEqualization=dict(argstr='--histogramEqualization ', ),
        method=dict(argstr='--method %s', ),
        modelConfigurationFilename=dict(
            argstr='--modelConfigurationFilename %s', ),
        modelFilename=dict(argstr='--modelFilename %s', ),
        multiStructureThreshold=dict(argstr='--multiStructureThreshold ', ),
        netConfiguration=dict(argstr='--netConfiguration %s', ),
        numberOfTrees=dict(argstr='--numberOfTrees %d', ),
        randomTreeDepth=dict(argstr='--randomTreeDepth %d', ),
        trainModel=dict(argstr='--trainModel ', ),
        trainModelStartIndex=dict(argstr='--trainModelStartIndex %d', ),
        validate=dict(argstr='--validate ', ),
        verbose=dict(argstr='--verbose %d', ),
    )
    inputs = BRAINSCut.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BRAINSCut_outputs():
    output_map = dict()
    outputs = BRAINSCut.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..developer import JistCortexSurfaceMeshInflation


def test_JistCortexSurfaceMeshInflation_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inLevelset=dict(argstr='--inLevelset %s', ),
        inLorentzian=dict(argstr='--inLorentzian %s', ),
        inMax=dict(argstr='--inMax %d', ),
        inMean=dict(argstr='--inMean %f', ),
        inSOR=dict(argstr='--inSOR %f', ),
        inStep=dict(argstr='--inStep %d', ),
        inTopology=dict(argstr='--inTopology %s', ),
        null=dict(argstr='--null %s', ),
        outInflated=dict(
            argstr='--outInflated %s',
            hash_files=False,
        ),
        outOriginal=dict(
            argstr='--outOriginal %s',
            hash_files=False,
        ),
        xDefaultMem=dict(argstr='-xDefaultMem %d', ),
        xMaxProcess=dict(
            argstr='-xMaxProcess %d',
            usedefault=True,
        ),
        xPrefExt=dict(argstr='--xPrefExt %s', ),
    )
    inputs = JistCortexSurfaceMeshInflation.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_JistCortexSurfaceMeshInflation_outputs():
    output_map = dict(
        outInflated=dict(),
        outOriginal=dict(),
    )
    outputs = JistCortexSurfaceMeshInflation.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

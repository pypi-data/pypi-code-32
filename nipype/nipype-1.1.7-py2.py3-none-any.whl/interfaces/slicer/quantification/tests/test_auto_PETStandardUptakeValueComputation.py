# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..petstandarduptakevaluecomputation import PETStandardUptakeValueComputation


def test_PETStandardUptakeValueComputation_inputs():
    input_map = dict(
        OutputLabel=dict(argstr='--OutputLabel %s', ),
        OutputLabelValue=dict(argstr='--OutputLabelValue %s', ),
        SUVMax=dict(argstr='--SUVMax %s', ),
        SUVMean=dict(argstr='--SUVMean %s', ),
        SUVMin=dict(argstr='--SUVMin %s', ),
        args=dict(argstr='%s', ),
        color=dict(argstr='--color %s', ),
        csvFile=dict(
            argstr='--csvFile %s',
            hash_files=False,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        labelMap=dict(argstr='--labelMap %s', ),
        petDICOMPath=dict(argstr='--petDICOMPath %s', ),
        petVolume=dict(argstr='--petVolume %s', ),
    )
    inputs = PETStandardUptakeValueComputation.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_PETStandardUptakeValueComputation_outputs():
    output_map = dict(csvFile=dict(), )
    outputs = PETStandardUptakeValueComputation.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

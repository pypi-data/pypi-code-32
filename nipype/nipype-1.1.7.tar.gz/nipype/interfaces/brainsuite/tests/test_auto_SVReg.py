# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..brainsuite import SVReg


def test_SVReg_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        atlasFilePrefix=dict(
            argstr="'%s'",
            position=1,
        ),
        curveMatchingInstructions=dict(argstr="'-cur %s'", ),
        dataSinkDelay=dict(argstr='%s', ),
        displayModuleName=dict(argstr="'-m'", ),
        displayTimestamps=dict(argstr="'-t'", ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        iterations=dict(argstr="'-H %d'", ),
        keepIntermediates=dict(argstr="'-k'", ),
        pialSurfaceMaskDilation=dict(argstr="'-D %d'", ),
        refineOutputs=dict(argstr="'-r'", ),
        shortMessages=dict(argstr="'-gui'", ),
        skipToIntensityReg=dict(argstr="'-p'", ),
        skipToVolumeReg=dict(argstr="'-s'", ),
        skipVolumetricProcessing=dict(argstr="'-S'", ),
        subjectFilePrefix=dict(
            argstr="'%s'",
            mandatory=True,
            position=0,
        ),
        useCerebrumMask=dict(argstr="'-C'", ),
        useManualMaskFile=dict(argstr="'-cbm'", ),
        useMultiThreading=dict(argstr="'-P'", ),
        useSingleThreading=dict(argstr="'-U'", ),
        verbosity0=dict(
            argstr="'-v0'",
            xor=('verbosity0', 'verbosity1', 'verbosity2'),
        ),
        verbosity1=dict(
            argstr="'-v1'",
            xor=('verbosity0', 'verbosity1', 'verbosity2'),
        ),
        verbosity2=dict(
            argstr="'v2'",
            xor=('verbosity0', 'verbosity1', 'verbosity2'),
        ),
    )
    inputs = SVReg.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value

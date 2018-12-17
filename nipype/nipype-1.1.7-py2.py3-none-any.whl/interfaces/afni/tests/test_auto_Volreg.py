# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import Volreg


def test_Volreg_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        basefile=dict(
            argstr='-base %s',
            position=-6,
        ),
        copyorigin=dict(argstr='-twodup', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            copyfile=False,
            mandatory=True,
            position=-1,
        ),
        in_weight_volume=dict(argstr="-weight '%s[%d]'", ),
        interp=dict(argstr='-%s', ),
        md1d_file=dict(
            argstr='-maxdisp1D %s',
            keep_extension=True,
            name_source='in_file',
            name_template='%s_md.1D',
            position=-4,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        oned_file=dict(
            argstr='-1Dfile %s',
            keep_extension=True,
            name_source='in_file',
            name_template='%s.1D',
        ),
        oned_matrix_save=dict(
            argstr='-1Dmatrix_save %s',
            keep_extension=True,
            name_source='in_file',
            name_template='%s.aff12.1D',
        ),
        out_file=dict(
            argstr='-prefix %s',
            name_source='in_file',
            name_template='%s_volreg',
        ),
        outputtype=dict(),
        timeshift=dict(argstr='-tshift 0', ),
        verbose=dict(argstr='-verbose', ),
        zpad=dict(
            argstr='-zpad %d',
            position=-5,
        ),
    )
    inputs = Volreg.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Volreg_outputs():
    output_map = dict(
        md1d_file=dict(),
        oned_file=dict(),
        oned_matrix_save=dict(),
        out_file=dict(),
    )
    outputs = Volreg.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

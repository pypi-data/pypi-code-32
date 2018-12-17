# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..dwi import DwiTool


def test_DwiTool_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        b0_file=dict(
            argstr='-b0 %s',
            position=4,
        ),
        ball_flag=dict(
            argstr='-ball',
            position=6,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag', 'dti_flag2',
                'ballv_flag', 'nod_flag', 'nodv_flag'
            ],
        ),
        ballv_flag=dict(
            argstr='-ballv',
            position=6,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag', 'dti_flag2', 'ball_flag',
                'nod_flag', 'nodv_flag'
            ],
        ),
        bval_file=dict(
            argstr='-bval %s',
            mandatory=True,
            position=2,
        ),
        bvec_file=dict(
            argstr='-bvec %s',
            position=3,
        ),
        diso_val=dict(argstr='-diso %f', ),
        dpr_val=dict(argstr='-dpr %f', ),
        dti_flag=dict(
            argstr='-dti',
            position=6,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag2', 'ball_flag',
                'ballv_flag', 'nod_flag', 'nodv_flag'
            ],
        ),
        dti_flag2=dict(
            argstr='-dti2',
            position=6,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag', 'ball_flag',
                'ballv_flag', 'nod_flag', 'nodv_flag'
            ],
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        famap_file=dict(
            argstr='-famap %s',
            name_source=['source_file'],
            name_template='%s_famap.nii.gz',
        ),
        ivim_flag=dict(
            argstr='-ivim',
            position=6,
            xor=[
                'mono_flag', 'dti_flag', 'dti_flag2', 'ball_flag',
                'ballv_flag', 'nod_flag', 'nodv_flag'
            ],
        ),
        logdti_file=dict(
            argstr='-logdti2 %s',
            name_source=['source_file'],
            name_template='%s_logdti2.nii.gz',
        ),
        mask_file=dict(
            argstr='-mask %s',
            position=5,
        ),
        mcmap_file=dict(
            argstr='-mcmap %s',
            name_source=['source_file'],
            name_template='%s_mcmap.nii.gz',
        ),
        mdmap_file=dict(
            argstr='-mdmap %s',
            name_source=['source_file'],
            name_template='%s_mdmap.nii.gz',
        ),
        mono_flag=dict(
            argstr='-mono',
            position=6,
            xor=[
                'ivim_flag', 'dti_flag', 'dti_flag2', 'ball_flag',
                'ballv_flag', 'nod_flag', 'nodv_flag'
            ],
        ),
        nod_flag=dict(
            argstr='-nod',
            position=6,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag', 'dti_flag2', 'ball_flag',
                'ballv_flag', 'nodv_flag'
            ],
        ),
        nodv_flag=dict(
            argstr='-nodv',
            position=6,
            xor=[
                'mono_flag', 'ivim_flag', 'dti_flag', 'dti_flag2', 'ball_flag',
                'ballv_flag', 'nod_flag'
            ],
        ),
        rgbmap_file=dict(
            argstr='-rgbmap %s',
            name_source=['source_file'],
            name_template='%s_rgbmap.nii.gz',
        ),
        source_file=dict(
            argstr='-source %s',
            mandatory=True,
            position=1,
        ),
        syn_file=dict(
            argstr='-syn %s',
            name_source=['source_file'],
            name_template='%s_syn.nii.gz',
            requires=['bvec_file', 'b0_file'],
        ),
        v1map_file=dict(
            argstr='-v1map %s',
            name_source=['source_file'],
            name_template='%s_v1map.nii.gz',
        ),
    )
    inputs = DwiTool.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DwiTool_outputs():
    output_map = dict(
        famap_file=dict(),
        logdti_file=dict(),
        mcmap_file=dict(),
        mdmap_file=dict(),
        rgbmap_file=dict(),
        syn_file=dict(),
        v1map_file=dict(),
    )
    outputs = DwiTool.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..diffusion import dtiprocess


def test_dtiprocess_inputs():
    input_map = dict(
        DTI_double=dict(argstr='--DTI_double ', ),
        RD_output=dict(
            argstr='--RD_output %s',
            hash_files=False,
        ),
        affineitk_file=dict(argstr='--affineitk_file %s', ),
        args=dict(argstr='%s', ),
        color_fa_output=dict(
            argstr='--color_fa_output %s',
            hash_files=False,
        ),
        correction=dict(argstr='--correction %s', ),
        deformation_output=dict(
            argstr='--deformation_output %s',
            hash_files=False,
        ),
        dof_file=dict(argstr='--dof_file %s', ),
        dti_image=dict(argstr='--dti_image %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fa_gradient_output=dict(
            argstr='--fa_gradient_output %s',
            hash_files=False,
        ),
        fa_gradmag_output=dict(
            argstr='--fa_gradmag_output %s',
            hash_files=False,
        ),
        fa_output=dict(
            argstr='--fa_output %s',
            hash_files=False,
        ),
        forward=dict(argstr='--forward %s', ),
        frobenius_norm_output=dict(
            argstr='--frobenius_norm_output %s',
            hash_files=False,
        ),
        hField=dict(argstr='--hField ', ),
        interpolation=dict(argstr='--interpolation %s', ),
        lambda1_output=dict(
            argstr='--lambda1_output %s',
            hash_files=False,
        ),
        lambda2_output=dict(
            argstr='--lambda2_output %s',
            hash_files=False,
        ),
        lambda3_output=dict(
            argstr='--lambda3_output %s',
            hash_files=False,
        ),
        mask=dict(argstr='--mask %s', ),
        md_output=dict(
            argstr='--md_output %s',
            hash_files=False,
        ),
        negative_eigenvector_output=dict(
            argstr='--negative_eigenvector_output %s',
            hash_files=False,
        ),
        newdof_file=dict(argstr='--newdof_file %s', ),
        outmask=dict(
            argstr='--outmask %s',
            hash_files=False,
        ),
        principal_eigenvector_output=dict(
            argstr='--principal_eigenvector_output %s',
            hash_files=False,
        ),
        reorientation=dict(argstr='--reorientation %s', ),
        rot_output=dict(
            argstr='--rot_output %s',
            hash_files=False,
        ),
        scalar_float=dict(argstr='--scalar_float ', ),
        sigma=dict(argstr='--sigma %f', ),
        verbose=dict(argstr='--verbose ', ),
    )
    inputs = dtiprocess.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_dtiprocess_outputs():
    output_map = dict(
        RD_output=dict(),
        color_fa_output=dict(),
        deformation_output=dict(),
        fa_gradient_output=dict(),
        fa_gradmag_output=dict(),
        fa_output=dict(),
        frobenius_norm_output=dict(),
        lambda1_output=dict(),
        lambda2_output=dict(),
        lambda3_output=dict(),
        md_output=dict(),
        negative_eigenvector_output=dict(),
        outmask=dict(),
        principal_eigenvector_output=dict(),
        rot_output=dict(),
    )
    outputs = dtiprocess.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

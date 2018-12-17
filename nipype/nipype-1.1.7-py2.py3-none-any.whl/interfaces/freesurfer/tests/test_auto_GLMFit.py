# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import GLMFit


def test_GLMFit_inputs():
    input_map = dict(
        allow_ill_cond=dict(argstr='--illcond', ),
        allow_repeated_subjects=dict(argstr='--allowsubjrep', ),
        args=dict(argstr='%s', ),
        calc_AR1=dict(argstr='--tar1', ),
        check_opts=dict(argstr='--checkopts', ),
        compute_log_y=dict(argstr='--logy', ),
        contrast=dict(argstr='--C %s...', ),
        cortex=dict(
            argstr='--cortex',
            xor=['label_file'],
        ),
        debug=dict(argstr='--debug', ),
        design=dict(
            argstr='--X %s',
            xor=('fsgd', 'design', 'one_sample'),
        ),
        diag=dict(argstr='--diag %d', ),
        diag_cluster=dict(argstr='--diag-cluster', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fixed_fx_dof=dict(
            argstr='--ffxdof %d',
            xor=['fixed_fx_dof_file'],
        ),
        fixed_fx_dof_file=dict(
            argstr='--ffxdofdat %d',
            xor=['fixed_fx_dof'],
        ),
        fixed_fx_var=dict(argstr='--yffxvar %s', ),
        force_perm=dict(argstr='--perm-force', ),
        fsgd=dict(
            argstr='--fsgd %s %s',
            xor=('fsgd', 'design', 'one_sample'),
        ),
        fwhm=dict(argstr='--fwhm %f', ),
        glm_dir=dict(
            argstr='--glmdir %s',
            genfile=True,
        ),
        hemi=dict(),
        in_file=dict(
            argstr='--y %s',
            copyfile=False,
            mandatory=True,
        ),
        invert_mask=dict(argstr='--mask-inv', ),
        label_file=dict(
            argstr='--label %s',
            xor=['cortex'],
        ),
        mask_file=dict(argstr='--mask %s', ),
        no_contrast_ok=dict(argstr='--no-contrasts-ok', ),
        no_est_fwhm=dict(argstr='--no-est-fwhm', ),
        no_mask_smooth=dict(argstr='--no-mask-smooth', ),
        no_prune=dict(
            argstr='--no-prune',
            xor=['prunethresh'],
        ),
        one_sample=dict(
            argstr='--osgm',
            xor=('one_sample', 'fsgd', 'design', 'contrast'),
        ),
        pca=dict(argstr='--pca', ),
        per_voxel_reg=dict(argstr='--pvr %s...', ),
        profile=dict(argstr='--profile %d', ),
        prune=dict(argstr='--prune', ),
        prune_thresh=dict(
            argstr='--prune_thr %f',
            xor=['noprune'],
        ),
        resynth_test=dict(argstr='--resynthtest %d', ),
        save_cond=dict(argstr='--save-cond', ),
        save_estimate=dict(argstr='--yhat-save', ),
        save_res_corr_mtx=dict(argstr='--eres-scm', ),
        save_residual=dict(argstr='--eres-save', ),
        seed=dict(argstr='--seed %d', ),
        self_reg=dict(argstr='--selfreg %d %d %d', ),
        sim_done_file=dict(argstr='--sim-done %s', ),
        sim_sign=dict(argstr='--sim-sign %s', ),
        simulation=dict(argstr='--sim %s %d %f %s', ),
        subject_id=dict(),
        subjects_dir=dict(),
        surf=dict(
            argstr='--surf %s %s %s',
            requires=['subject_id', 'hemi'],
        ),
        surf_geo=dict(usedefault=True, ),
        synth=dict(argstr='--synth', ),
        uniform=dict(argstr='--uniform %f %f', ),
        var_fwhm=dict(argstr='--var-fwhm %f', ),
        vox_dump=dict(argstr='--voxdump %d %d %d', ),
        weight_file=dict(xor=['weighted_ls'], ),
        weight_inv=dict(
            argstr='--w-inv',
            xor=['weighted_ls'],
        ),
        weight_sqrt=dict(
            argstr='--w-sqrt',
            xor=['weighted_ls'],
        ),
        weighted_ls=dict(
            argstr='--wls %s',
            xor=('weight_file', 'weight_inv', 'weight_sqrt'),
        ),
    )
    inputs = GLMFit.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_GLMFit_outputs():
    output_map = dict(
        beta_file=dict(),
        dof_file=dict(),
        error_file=dict(),
        error_stddev_file=dict(),
        error_var_file=dict(),
        estimate_file=dict(),
        frame_eigenvectors=dict(),
        ftest_file=dict(),
        fwhm_file=dict(),
        gamma_file=dict(),
        gamma_var_file=dict(),
        glm_dir=dict(),
        mask_file=dict(),
        sig_file=dict(),
        singular_values=dict(),
        spatial_eigenvectors=dict(),
        svd_stats_file=dict(),
    )
    outputs = GLMFit.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import MRIsCALabel


def test_MRIsCALabel_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        aseg=dict(argstr='-aseg %s', ),
        canonsurf=dict(
            argstr='%s',
            mandatory=True,
            position=-3,
        ),
        classifier=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        copy_inputs=dict(),
        curv=dict(mandatory=True, ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        hemisphere=dict(
            argstr='%s',
            mandatory=True,
            position=-4,
        ),
        label=dict(argstr='-l %s', ),
        num_threads=dict(),
        out_file=dict(
            argstr='%s',
            hash_files=False,
            keep_extension=True,
            name_source=['hemisphere'],
            name_template='%s.aparc.annot',
            position=-1,
        ),
        seed=dict(argstr='-seed %d', ),
        smoothwm=dict(mandatory=True, ),
        subject_id=dict(
            argstr='%s',
            mandatory=True,
            position=-5,
            usedefault=True,
        ),
        subjects_dir=dict(),
        sulc=dict(mandatory=True, ),
    )
    inputs = MRIsCALabel.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_MRIsCALabel_outputs():
    output_map = dict(out_file=dict(), )
    outputs = MRIsCALabel.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

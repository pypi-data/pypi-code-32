# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..tensors import DWI2SphericalHarmonicsImage


def test_DWI2SphericalHarmonicsImage_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        encoding_file=dict(
            argstr='-grad %s',
            mandatory=True,
            position=1,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        maximum_harmonic_order=dict(argstr='-lmax %s', ),
        normalise=dict(
            argstr='-normalise',
            position=3,
        ),
        out_filename=dict(
            argstr='%s',
            genfile=True,
            position=-1,
        ),
    )
    inputs = DWI2SphericalHarmonicsImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DWI2SphericalHarmonicsImage_outputs():
    output_map = dict(spherical_harmonics_image=dict(), )
    outputs = DWI2SphericalHarmonicsImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

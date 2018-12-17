# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..fix import Classifier


def test_Classifier_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        artifacts_list_file=dict(),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        mel_ica=dict(
            argstr='%s',
            copyfile=False,
            position=1,
        ),
        thresh=dict(
            argstr='%d',
            mandatory=True,
            position=-1,
        ),
        trained_wts_file=dict(
            argstr='%s',
            copyfile=False,
            mandatory=True,
            position=2,
        ),
    )
    inputs = Classifier.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Classifier_outputs():
    output_map = dict(artifacts_list_file=dict(), )
    outputs = Classifier.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

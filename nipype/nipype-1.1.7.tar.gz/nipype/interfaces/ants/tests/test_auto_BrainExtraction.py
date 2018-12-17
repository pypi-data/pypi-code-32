# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..segmentation import BrainExtraction


def test_BrainExtraction_inputs():
    input_map = dict(
        anatomical_image=dict(
            argstr='-a %s',
            mandatory=True,
        ),
        args=dict(argstr='%s', ),
        brain_probability_mask=dict(
            argstr='-m %s',
            copyfile=False,
            mandatory=True,
        ),
        brain_template=dict(
            argstr='-e %s',
            mandatory=True,
        ),
        debug=dict(argstr='-z 1', ),
        dimension=dict(
            argstr='-d %d',
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        extraction_registration_mask=dict(argstr='-f %s', ),
        image_suffix=dict(
            argstr='-s %s',
            usedefault=True,
        ),
        keep_temporary_files=dict(argstr='-k %d', ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_prefix=dict(
            argstr='-o %s',
            usedefault=True,
        ),
        use_floatingpoint_precision=dict(argstr='-q %d', ),
        use_random_seeding=dict(argstr='-u %d', ),
    )
    inputs = BrainExtraction.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_BrainExtraction_outputs():
    output_map = dict(
        BrainExtractionBrain=dict(),
        BrainExtractionCSF=dict(),
        BrainExtractionGM=dict(),
        BrainExtractionInitialAffine=dict(),
        BrainExtractionInitialAffineFixed=dict(),
        BrainExtractionInitialAffineMoving=dict(),
        BrainExtractionLaplacian=dict(),
        BrainExtractionMask=dict(),
        BrainExtractionPrior0GenericAffine=dict(),
        BrainExtractionPrior1InverseWarp=dict(),
        BrainExtractionPrior1Warp=dict(),
        BrainExtractionPriorWarped=dict(),
        BrainExtractionSegmentation=dict(),
        BrainExtractionTemplateLaplacian=dict(),
        BrainExtractionTmp=dict(),
        BrainExtractionWM=dict(),
        N4Corrected0=dict(),
        N4Truncated0=dict(),
    )
    outputs = BrainExtraction.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..misc import SplitROIs


def test_SplitROIs_inputs():
    input_map = dict(
        in_file=dict(mandatory=True, ),
        in_mask=dict(),
        roi_size=dict(),
    )
    inputs = SplitROIs.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SplitROIs_outputs():
    output_map = dict(
        out_files=dict(),
        out_index=dict(),
        out_masks=dict(),
    )
    outputs = SplitROIs.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

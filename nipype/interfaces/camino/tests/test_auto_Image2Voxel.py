# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..convert import Image2Voxel


def test_Image2Voxel_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-4dimage %s',
            extensions=None,
            mandatory=True,
            position=1,
        ),
        out_file=dict(
            argstr='> %s',
            genfile=True,
            position=-1,
        ),
        out_type=dict(
            argstr='-outputdatatype %s',
            position=2,
            usedefault=True,
        ),
    )
    inputs = Image2Voxel.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Image2Voxel_outputs():
    output_map = dict(voxel_order=dict(extensions=None, ), )
    outputs = Image2Voxel.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

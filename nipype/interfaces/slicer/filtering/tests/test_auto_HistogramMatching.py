# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..histogrammatching import HistogramMatching


def test_HistogramMatching_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputVolume=dict(
            argstr='%s',
            extensions=None,
            position=-3,
        ),
        numberOfHistogramLevels=dict(argstr='--numberOfHistogramLevels %d', ),
        numberOfMatchPoints=dict(argstr='--numberOfMatchPoints %d', ),
        outputVolume=dict(
            argstr='%s',
            hash_files=False,
            position=-1,
        ),
        referenceVolume=dict(
            argstr='%s',
            extensions=None,
            position=-2,
        ),
        threshold=dict(argstr='--threshold ', ),
    )
    inputs = HistogramMatching.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_HistogramMatching_outputs():
    output_map = dict(
        outputVolume=dict(
            extensions=None,
            position=-1,
        ), )
    outputs = HistogramMatching.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value

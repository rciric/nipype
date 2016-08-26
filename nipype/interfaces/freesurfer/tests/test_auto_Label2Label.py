# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..model import Label2Label


def test_Label2Label_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    copy_inputs=dict(),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    hemisphere=dict(argstr='--hemi %s',
    mandatory=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(argstr='--trglabel %s',
    hash_files=False,
    keep_extension=True,
    name_source=[u'source_label'],
    name_template='%s_converted',
    ),
    registration_method=dict(argstr='--regmethod %s',
    usedefault=True,
    ),
    source_label=dict(argstr='--srclabel %s',
    mandatory=True,
    ),
    source_sphere_reg=dict(mandatory=True,
    ),
    source_subject=dict(argstr='--srcsubject %s',
    mandatory=True,
    ),
    source_white=dict(mandatory=True,
    ),
    sphere_reg=dict(mandatory=True,
    ),
    subject_id=dict(argstr='--trgsubject %s',
    mandatory=True,
    usedefault=True,
    ),
    subjects_dir=dict(),
    terminal_output=dict(nohash=True,
    ),
    white=dict(mandatory=True,
    ),
    )
    inputs = Label2Label.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Label2Label_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Label2Label.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

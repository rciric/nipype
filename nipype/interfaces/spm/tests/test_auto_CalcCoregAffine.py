# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.spm.utils import CalcCoregAffine

def test_CalcCoregAffine_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    invmat=dict(),
    mat=dict(),
    matlab_cmd=dict(),
    mfile=dict(usedefault=True,
    ),
    moving=dict(copyfile=False,
    mandatory=True,
    ),
    paths=dict(),
    target=dict(mandatory=True,
    ),
    use_mcr=dict(),
    use_v8struct=dict(min_ver='8',
    usedefault=True,
    ),
    )
    inputs = CalcCoregAffine.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_CalcCoregAffine_outputs():
    output_map = dict(invmat=dict(),
    mat=dict(),
    )
    outputs = CalcCoregAffine.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

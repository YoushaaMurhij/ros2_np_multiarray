import pytest
from ros2_np_multiarray import ros2_np_multiarray as rnm
import numpy as np

@pytest.mark.linter
@pytest.mark.pep257
def test_to_multiarray_f32():
    a, b, c, d = 1.0, 2.0, 3.0, 4.0
    Array = np.array([[[a, b], [c, d]]], dtype=np.float32)
    msg = rnm.to_multiarray_f32(Array)
    assert msg.layout.dim[0].label == 'dim0'
    assert msg.layout.dim[0].size == 1
    assert msg.layout.dim[0].stride == 4
    assert msg.layout.dim[1].label == 'dim1'
    assert msg.layout.dim[1].size == 2
    assert msg.layout.dim[1].stride == 8
    assert msg.layout.dim[2].label == 'dim2'
    assert msg.layout.dim[2].size == 2
    assert msg.layout.dim[2].stride == 8
    assert msg.layout.data_offset == 0
    assert msg.data == [a, b, c, d], 'Data is not equal to the original array'



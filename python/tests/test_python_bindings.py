import pybind11numpyexample
import numpy as np

def test_pybind11_numpy_example():
    assert pybind11numpyexample.vector_as_list(0) == []
    assert pybind11numpyexample.vector_as_list(3) == [0, 1, 2]

    a0 = pybind11numpyexample.vector_as_array(0)
    assert type(a0) == np.ndarray
    assert len(a0) == 0
    assert a0.dtype == np.int16
    a3 = pybind11numpyexample.vector_as_array(3)
    assert type(a3) == np.ndarray
    assert len(a3) == 3
    assert a3.dtype == np.int16
    assert a3[0] == 0
    assert a3[1] == 1
    assert a3[2] == 2

import pybind11numpyexample


def test_pybind11_numpy_example():
    assert pybind11numpyexample.vector_as_list(0) == []
    assert pybind11numpyexample.vector_as_list(3) == [0, 1, 2]

import pybind11numpyexample


def test_pybind11_numpy_example():
    assert pybind11numpyexample.add_one(1) == 2

import pybind11_numpy_example as pne
import numpy as np
import pytest


n_values = [0, 1, 2, 17, 159]


@pytest.mark.parametrize("list_func", [pne.pure_python_list, pne.vector_as_list])
@pytest.mark.parametrize("n", n_values)
def test_pybind11_numpy_example_list(list_func, n):
    l = list_func(n)
    assert isinstance(l, list)
    assert len(l) == n
    for i in range(n):
        assert l[i] == i


@pytest.mark.parametrize(
    "ndarray_func", [pne.vector_as_array, pne.vector_as_array_nocopy]
)
@pytest.mark.parametrize("n", n_values)
def test_pybind11_numpy_example_ndarray(ndarray_func, n):
    a = ndarray_func(n)
    assert isinstance(a, np.ndarray)
    assert len(a) == n
    assert a.dtype == np.int16
    for i in range(n):
        assert a[i] == i

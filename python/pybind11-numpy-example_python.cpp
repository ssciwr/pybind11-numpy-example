#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "pybind11-numpy-example/pybind11-numpy-example.hpp"

namespace py = pybind11;

namespace pybind11numpyexample {

PYBIND11_MODULE(pybind11numpyexample, m)
{
  m.doc() = "Python Bindings for pybind11-numpy-example";
  m.def("vector_as_list", &vector_as_list, "Returns a vector of ints as a Python List");
}

} // namespace pybind11numpyexample

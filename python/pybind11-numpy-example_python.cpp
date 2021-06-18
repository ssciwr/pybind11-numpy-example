#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "pybind11-numpy-example/pybind11-numpy-example.hpp"

namespace py = pybind11;

namespace pybind11numpyexample {

PYBIND11_MODULE(pybind11numpyexample, m)
{
  m.doc() = "Python Bindings for pybind11-numpy-example";
  m.def("add_one", &add_one, "Increments an integer value");
}

} // namespace pybind11numpyexample

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>

#include "pybind11-numpy-example/pybind11-numpy-example.hpp"

namespace py = pybind11;

namespace pybind11numpyexample {

/** @brief Return a vector as a Python List
 *
 * @param size The size of the vector to return
 * @returns the vector as a Python List
 */
static std::vector<short> vector_as_list(std::size_t size) {
  return make_vector<short>(size);
}

/** @brief Return a vector as a NumPy array
 *
 * Makes a copy of an existing vector of data
 *
 * @param size The size of the vector to return
 * @returns the vector as a NumPy array
 */
static py::array_t<short> vector_as_array(std::size_t size) {
  auto temp_vector = make_vector<short>(size);
  return py::array(size, temp_vector.data());
}

PYBIND11_MODULE(pybind11numpyexample, m)
{
  m.doc() = "Python Bindings for pybind11-numpy-example";
  m.def("vector_as_list", &vector_as_list, "Returns a vector of 16-bit ints as a Python List");
  m.def("vector_as_array", &vector_as_array, "Returns a vector of 16-bit ints as a NumPy array");
}


} // namespace pybind11numpyexample

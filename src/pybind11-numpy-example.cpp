#include "pybind11-numpy-example/pybind11-numpy-example.hpp"

#include <numeric>

namespace pybind11numpyexample {

template <typename T>
static std::vector<T> make_vector(std::size_t size){
  std::vector<T> v(size, 0);
  std::iota(v.begin(), v.end(), 0);
  return v;
}

std::vector<int> vector_as_list(std::size_t size){
  return make_vector<int>(size);
}

} // namespace pybind11numpyexample
#pragma once

#include <vector>

namespace pybind11numpyexample {

/** @brief Return a vector as a Python List
 *
 * @param size The size of the vector to return
 * @returns the vector as a Python List
 */
std::vector<int> vector_as_list(std::size_t size);

} // namespace pybind11numpyexample

#include "pybind11-numpy-example/pybind11-numpy-example.hpp"
#include "catch2/catch.hpp"

using namespace pybind11numpyexample;

TEST_CASE( "vector_as_list", "[vector_as_list]" ){
  REQUIRE(vector_as_list(0) == std::vector<int>{0});
  REQUIRE(vector_as_list(5) == std::vector<int>{0, 1, 2, 3, 4});
}
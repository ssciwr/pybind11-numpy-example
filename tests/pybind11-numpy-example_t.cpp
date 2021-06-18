#include "pybind11-numpy-example/pybind11-numpy-example.hpp"
#include "catch2/catch.hpp"

using namespace pybind11numpyexample;

TEST_CASE( "make_vector", "[make_vector]" ){
  REQUIRE(make_vector<int>(0) == std::vector<int>{0});
  REQUIRE(make_vector<int>(5) == std::vector<int>{0, 1, 2, 3, 4});
}
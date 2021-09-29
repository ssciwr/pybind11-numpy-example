#include "catch2/catch.hpp"
#include "pybind11-numpy-example/pybind11-numpy-example.hpp"

using namespace pybind11numpyexample;

TEST_CASE("make_vector", "[make_vector]") {
  REQUIRE(make_vector<int>(0) == std::vector<int>{});
  REQUIRE(make_vector<int>(5) == std::vector<int>{0, 1, 2, 3, 4});
  REQUIRE(make_vector<short>(3) == std::vector<short>{0, 1, 2});
  REQUIRE(make_vector<std::size_t>(4) == std::vector<std::size_t>{0, 1, 2, 3});
}

add_executable(tests tests.cpp pybind11-numpy-example_t.cpp)
target_link_libraries(tests PUBLIC pybind11-numpy-example Catch2::Catch2)

# allow user to run tests with `make test` or `ctest`
catch_discover_tests(tests)

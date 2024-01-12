add_executable(tests pybind11_numpy_example_t.cpp)
target_link_libraries(tests PUBLIC pybind11_numpy_example
                                   Catch2::Catch2WithMain)

# allow user to run tests with `make test` or `ctest`
catch_discover_tests(tests)

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(pybind11numpyexample_python
                    pybind11-numpy-example_python.cpp)
target_link_libraries(pybind11numpyexample_python PUBLIC pybind11-numpy-example)
set_target_properties(pybind11numpyexample_python
                      PROPERTIES OUTPUT_NAME pybind11numpyexample)
install(TARGETS pybind11numpyexample_python DESTINATION .)

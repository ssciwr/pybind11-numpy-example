find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(_pybind11_numpy_example pybind11_numpy_example_python.cpp)
target_link_libraries(_pybind11_numpy_example PUBLIC pybind11_numpy_example)
install(TARGETS _pybind11_numpy_example DESTINATION pybind11_numpy_example)

add_library(pybind11_numpy_example pybind11_numpy_example.cpp)
target_include_directories(
  pybind11_numpy_example
  PUBLIC $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include/>
         $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

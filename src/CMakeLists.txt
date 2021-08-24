add_library(pybind11-numpy-example pybind11-numpy-example.cpp)
target_include_directories(
  pybind11-numpy-example
  PUBLIC $<BUILD_INTERFACE:${CMAKE_SOURCE_DIR}/include/>
         $<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>)

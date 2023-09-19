cmake_minimum_required(VERSION 3.15..3.26)

# Set a name and a version number for your project:
project(
  pybind11-numpy-example
  VERSION 0.0.7
  LANGUAGES CXX)

# Initialize some default paths
include(GNUInstallDirs)

# Define the minimum C++ standard that is required
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

# Configuration options
option(BUILD_PYTHON "Enable building of Python bindings" ON)
option(BUILD_DOCS "Enable building of documentation" ON)

# Build the library
add_subdirectory(src)

# Build the tests
include(CTest)
if(BUILD_TESTING)
  add_subdirectory(ext/Catch2)
  include(./ext/Catch2/extras/Catch.cmake)
  add_subdirectory(tests)
endif()

# Build the documentation
if(BUILD_DOCS)
  add_subdirectory(doc)
endif()

# Build the python bindings
if(BUILD_PYTHON)
  add_subdirectory(python)
endif()

# Add an alias target for use if this project is included as a subproject in
# another project
add_library(pybind11-numpy-example::pybind11-numpy-example ALIAS
            pybind11-numpy-example)

# Install targets and configuration
install(
  TARGETS pybind11-numpy-example
  EXPORT pybind11-numpy-example-config
  RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
  LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
  ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR})

install(
  EXPORT pybind11-numpy-example-config
  NAMESPACE pybind11-numpy-example::
  DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/pybind11-numpy-example)

install(DIRECTORY ${CMAKE_CURRENT_LIST_DIR}/include/
        DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})

# This prints a summary of found dependencies
include(FeatureSummary)
feature_summary(WHAT ALL)

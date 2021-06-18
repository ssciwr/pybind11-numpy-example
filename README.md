# pybind11-numpy-example

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/lkeegan/pybind11-numpy-example/CI)](https://github.com/lkeegan/pybind11-numpy-example/actions?query=workflow%3ACI)
[![PyPI Release](https://img.shields.io/pypi/v/pybind11numpyexample.svg)](https://pypi.org/project/pybind11numpyexample)
[![Documentation Status](https://readthedocs.org/projects/pybind11-numpy-example/badge/)](https://pybind11-numpy-example.readthedocs.io/)
[![codecov](https://codecov.io/gh/lkeegan/pybind11-numpy-example/branch/main/graph/badge.svg)](https://codecov.io/gh/lkeegan/pybind11-numpy-example)


# Prerequisites

Building pybind11-numpy-example requires the following software installed:

* A C++11-compliant compiler
* CMake `>= 3.9`
* Doxygen (optional, documentation building is skipped if missing)* Python `>= 3.6` for building Python bindings

# Building pybind11-numpy-example

The following sequence of commands builds pybind11-numpy-example.
It assumes that your current working directory is the top-level directory
of the freshly cloned repository:

```
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release ..
cmake --build .
```

The build process can be customized with the following CMake variables,
which can be set by adding `-D<var>={ON, OFF}` to the `cmake` call:

* `BUILD_TESTING`: Enable building of the test suite (default: `ON`)
* `BUILD_DOCS`: Enable building the documentation (default: `ON`)
* `BUILD_PYTHON`: Enable building the Python bindings (default: `ON`)

# Documentation

pybind11-numpy-example provides a Sphinx-based documentation, that can
be browsed [online at readthedocs.org](https://pybind11-numpy-example.readthedocs.io).

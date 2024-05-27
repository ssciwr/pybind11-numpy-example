# pybind11-numpy-example

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI Release](https://img.shields.io/pypi/v/pybind11-numpy-example.svg)](https://pypi.org/project/pybind11-numpy-example)
[![Conda Release](https://img.shields.io/conda/v/conda-forge/pybind11-numpy-example)](https://anaconda.org/conda-forge/pybind11-numpy-example)
[![Python Versions](https://img.shields.io/pypi/pyversions/pybind11-numpy-example)](https://pypi.org/project/pybind11-numpy-example)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/lkeegan/pybind11-numpy-example/ci.yml?branch=main)](https://github.com/lkeegan/pybind11-numpy-example/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/pybind11-numpy-example/badge/)](https://pybind11-numpy-example.readthedocs.io/)

# What

A simple example of how to use [pybind11](https://github.com/pybind/pybind11) with [numpy](https://numpy.org/) and publish this as a library on [PyPI](https://pypi.org/project/pybind11-numpy-example/) and [conda-forge](https://anaconda.org/conda-forge/pybind11-numpy-example).

This C++/Python library creates a `std::vector` of 16-bit ints,
and provides a Python interface to the contents of this vector in a few different ways:

- a Python [List](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) (copy the data)
- a NumPy [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) (copy the data).
- a NumPy [ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) (move the data).

# Why

Python Lists are great!
However, when storing many small elements of the same type,
a Numpy array is much faster and uses a lot less memory:

![Memory used vs number of elements](https://raw.githubusercontent.com/ssciwr/pybind11-numpy-example/main/scripts/memory.png)

![Time used vs number of elements](https://raw.githubusercontent.com/ssciwr/pybind11-numpy-example/main/scripts/time.png)

# How

The pybind11 code is in [src/pybind11_numpy_example_python.cpp](https://github.com/ssciwr/pybind11-numpy-example/blob/main/src/pybind11_numpy_example_python.cpp).

The python package is defined in [pyproject.toml](https://github.com/ssciwr/pybind11-numpy-example/blob/main/pyproject.toml)
and uses [scikit-build-core](https://github.com/scikit-build/scikit-build-core).

Each tagged commit triggers a [GitHub action job](https://github.com/ssciwr/pybind11-numpy-example/actions/workflows/pypi.yml)
which uses [cibuildwheel](https://cibuildwheel.readthedocs.io/) to build and upload a new release including binary wheels for all platforms to [PyPI](https://pypi.org/project/pybind11-numpy-example/).

The [conda-forge package](https://anaconda.org/conda-forge/pybind11-numpy-example) is generated from [this recipe](https://github.com/conda-forge/pybind11-numpy-example-feedstock/blob/main/recipe/meta.yaml), and automatically updates when a new version is uploaded to PyPI.

The scripts used to generate the above plots are in [scripts](https://github.com/ssciwr/pybind11-numpy-example/tree/main/scripts).

This repo was quickly set up using the SSC [C++ Project Cookiecutter](https://github.com/ssciwr/cookiecutter-cpp-project).

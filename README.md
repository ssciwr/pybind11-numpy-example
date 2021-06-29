# pybind11-numpy-example

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/lkeegan/pybind11-numpy-example/CI)](https://github.com/lkeegan/pybind11-numpy-example/actions?query=workflow%3ACI)
[![PyPI Release](https://img.shields.io/pypi/v/pybind11numpyexample.svg)](https://pypi.org/project/pybind11numpyexample)
[![Documentation Status](https://readthedocs.org/projects/pybind11-numpy-example/badge/)](https://pybind11-numpy-example.readthedocs.io/)

# What

A simple example of how to use [pybind11](https://github.com/pybind/pybind11) with [numpy](https://numpy.org/).

This C++/Python library creates a `std::vector` of 16-bit ints,
and exposes it either as a Python List or as a NumPy array.

# Why

Python Lists are great!
However, for the specific use case of storing many small elements of the same type,
a Numpy array is faster and uses a lot less memory:

![Memory used vs number of elements](scripts/memory.png)

![Time used vs number of elements](scripts/time.png)

[scripts/memory.png]

# How

See [python/pybind11-numpy-example_python.cpp](python/pybind11-numpy-example_python.cpp) for how to do this in C++ using pybind11.

The scripts used to generate the above plots are in [scripts](scripts) 

This repo was quickly set up using the SSC [C++ Project Cookiecutter](https://github.com/ssciwr/cookiecutter-cpp-project)
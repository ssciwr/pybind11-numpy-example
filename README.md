# pybind11-numpy-example

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/lkeegan/pybind11-numpy-example/CI)](https://github.com/lkeegan/pybind11-numpy-example/actions?query=workflow%3ACI)
[![PyPI Release](https://img.shields.io/pypi/v/pybind11numpyexample.svg)](https://pypi.org/project/pybind11numpyexample)
[![Documentation Status](https://readthedocs.org/projects/pybind11-numpy-example/badge/)](https://pybind11-numpy-example.readthedocs.io/)

# What

A simple example of how to use [pybind11](https://github.com/pybind/pybind11) with [numpy](https://numpy.org/).

This python library simply returns a vector of ints, either as a Python List or as a NumPy array.

# Why

For many use cases, Python Lists are slow to access and use a lot of memory compared to a NumPy array.

# About

This repo was quickly set up using the SSC [C++ Project Cookiecutter](https://github.com/ssciwr/cookiecutter-cpp-project)
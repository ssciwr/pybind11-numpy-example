----------------------
pybind11-numpy-example
----------------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:

What
====

A simple example of how to use
`pybind11 <https://github.com/pybind/pybind11>`__ with
`numpy <https://numpy.org/>`__.

This C++/Python library creates a ``std::vector`` of 16-bit ints,
and provides a Python interface to the contents of this vector in a
few different ways:

-  a Python
   `List <https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>`__
   (copy the data)
-  a NumPy
   `ndarray <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html>`__
   (copy the data).
-  a NumPy
   `ndarray <https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html>`__
   (move the data).

Why
===

Python Lists are great!
However, when storing many small elements of the same type,
a Numpy array is much faster and uses a lot less memory:

|Memory used vs number of elements|

|Time used vs number of elements|

How
===

The pybind11 code is in
`python/pybind11-numpy-example\_python.cpp <https://github.com/ssciwr/pybind11-numpy-example/blob/main/python/pybind11-numpy-example_python.cpp>`__.

The scripts used to generate the above plots are in
`scripts <https://github.com/ssciwr/pybind11-numpy-example/tree/main/scripts>`__.

This repo was quickly set up using the SSC `C++ Project
Cookiecutter <https://github.com/ssciwr/cookiecutter-cpp-project>`__.

.. |License: MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
.. |GitHub Workflow Status| image:: https://img.shields.io/github/workflow/status/lkeegan/pybind11-numpy-example/CI
   :target: https://github.com/lkeegan/pybind11-numpy-example/actions?query=workflow%3ACI
.. |PyPI Release| image:: https://img.shields.io/pypi/v/pybind11-numpy-example.svg
   :target: https://pypi.org/project/pybind11-numpy-example
.. |Documentation Status| image:: https://readthedocs.org/projects/pybind11-numpy-example/badge/
   :target: https://pybind11-numpy-example.readthedocs.io/
.. |Memory used vs number of elements| image:: https://raw.githubusercontent.com/ssciwr/pybind11-numpy-example/main/scripts/memory.png
.. |Time used vs number of elements| image:: https://raw.githubusercontent.com/ssciwr/pybind11-numpy-example/main/scripts/time.png

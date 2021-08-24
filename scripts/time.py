#!/usr/bin/env python

# simple script to print approx time taken

import pybind11numpyexample
import timeit
import sys

n = int(sys.argv[1])
data_type = int(sys.argv[2])
iters = 1 + 10000000 // n


def doit():
    if data_type == 0:
        return pybind11numpyexample.vector_as_list(n)
    elif data_type == 1:
        return pybind11numpyexample.vector_as_array(n)
    elif data_type == 2:
        return pybind11numpyexample.vector_as_array_nocopy(n)


print(timeit.timeit(doit, number=iters) / iters)

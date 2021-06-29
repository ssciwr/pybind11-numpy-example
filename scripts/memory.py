#!/usr/bin/env python

# simple script to print approx memory usage

import pybind11numpyexample
import resource
import sys

n=int(sys.argv[1])
data_type=int(sys.argv[2])
max_mem_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

if(data_type == 0):
    a = pybind11numpyexample.vector_as_list(n)
elif(data_type == 1):
    a = pybind11numpyexample.vector_as_array(n)
elif(data_type == 2):
    a = pybind11numpyexample.vector_as_array_nocopy(n)

max_mem_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

print(max_mem_after - max_mem_before)


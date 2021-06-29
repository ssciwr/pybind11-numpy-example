#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

mem_list = np.loadtxt("mem_list.txt")
mem_array = np.loadtxt("mem_array.txt")
mem_array_nocopy = np.loadtxt("mem_array_nocopy.txt")

plt.figure()
plt.title("RAM used vs number of elements")
plt.xlabel("Number of elements (million)")
plt.ylabel("RAM used (GB)")
plt.plot(mem_list[:,0]/1e6, mem_list[:,1]/1e6, label="list", marker="o")
plt.plot(mem_array[:,0]/1e6, mem_array[:,1]/1e6, label="array (copy)", marker="x")
plt.plot(mem_array_nocopy[:,0]/1e6, mem_array_nocopy[:,1]/1e6, label="array (move)", marker=".")
plt.legend()
plt.savefig('memory.png', bbox_inches='tight')

time_list = np.loadtxt("time_list.txt")
time_array = np.loadtxt("time_array.txt")
time_array_nocopy = np.loadtxt("time_array_nocopy.txt")

plt.figure()
plt.title("Time used vs number of elements")
plt.xlabel("Number of elements (million)")
plt.ylabel("Time used (seconds)")
plt.plot(time_list[:,0]/1e6, time_list[:,1], label="list", marker="o")
plt.plot(time_array[:,0]/1e6, time_array[:,1], label="array (copy)", marker="x")
plt.plot(time_array_nocopy[:,0]/1e6, time_array_nocopy[:,1], label="array (move)", marker=".")
plt.legend()
plt.savefig('time.png', bbox_inches='tight')

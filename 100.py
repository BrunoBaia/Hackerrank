"""Shape and Reshape

https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=false

Task

You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array."""


import numpy as np

array = np.array(list(map(int, input().split())))
print(np.reshape(array, [3, 3]))

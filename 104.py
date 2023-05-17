"""Zeros and Ones

https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=false

Task

You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions,
your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones."""


import numpy as np

shape = list(map(int, input().split()))
print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))

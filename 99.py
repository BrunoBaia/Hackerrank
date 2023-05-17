"""Arrays

https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=false

Task

You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float."""


import numpy


def arrays(arra):
    arr = numpy.array(arra, float)
    return numpy.flip(arr)


ar = input().strip().split(' ')
result = arrays(ar)
print(result)

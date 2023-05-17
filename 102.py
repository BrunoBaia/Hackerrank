"""Transpose and Flatten

https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=false

Task

You are given a nXm integer array matrix with space separated elements (n = rows and m = columns).
Your task is to print the transpose and flatten results."""


import numpy

array = [list(map(int, input().split())) for _ in range(int(input().split()[0]))]
array = numpy.array(array)
print(numpy.transpose(array))
print(array.flatten())

"""Concatenate

https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=false

Task

You are given two integer arrays of size nXp and mpX (n & m are rows, and p is the column).
Your task is to concatenate the arrays along axis 0."""


import numpy

n, m, p = map(int, input().split())
array_1 = numpy.array([list(map(int, input().split())) for _ in range(n)])
array_2 = numpy.array([list(map(int, input().split())) for _ in range(m)])
print(numpy.concatenate((array_1, array_2), axis=0))

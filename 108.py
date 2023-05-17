"""Sum and Prod

https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=false

Task

You are given a 2-D array with dimensions nXm.
Your task is to perform the sun tool over axis 0 and then find the product of that result."""


import numpy

n, m = input().split()
array = [list(map(int, input().split())) for _ in range(int(n))]
print(numpy.prod(numpy.sum(array, axis=0)))

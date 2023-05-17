"""Min and Max

https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=false

Task

You are given a 2-D array with dimensions nXm.
Your task is to perform the min function over axis 1 and then find the max of that."""


import numpy as np

n, m = map(int, input().split())
array = []
for line in range(n):
    inp = list(map(int, input().split()))
    array.append(inp)

array = np.array(array)
result = max(np.min(array, axis=1))
print(result)

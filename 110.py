"""Mean, Var, and Std

https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=false

Task

You are given a 2-D array of size nXm.
Your task is to find:
The mean along axis 1.
The var along axis 0.
The std along axis None"""


import numpy as np

n, m = map(int, input().split())
np_array = np.array([list(map(int, input().split())) for lista in range(n)])
print(np.mean(np_array, axis=1))
print(np.var(np_array, axis=0))
print(round(np.std(np_array), 11))

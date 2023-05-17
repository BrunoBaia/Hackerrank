"""Inner and Outer

https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=false

Task

You are given two arrays: a and b.
Your task is to compute their inner and outer product."""


import numpy as np

a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(np.inner(a, b))
print(np.outer(a, b))

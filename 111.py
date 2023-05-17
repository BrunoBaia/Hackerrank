"""Dot and Cross

https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=false

Task

You are given two arrays a and b. Both have dimensions of nXm.
Your task is to compute their matrix product."""


import numpy as np

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
print(np.dot(a, b))

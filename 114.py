"""Linear Algebra

https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=false

Task

You are given a square matrix a with dimensions nXm. Your task is to find the determinant.
Note: Round the answer to 2 places after the decimal."""


import numpy as np

n = int(input())
arr = [list(map(float, input().split())) for _ in range(n)]
result = np.linalg.det(arr)
print(round(result, 2))

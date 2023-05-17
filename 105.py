"""Eye and Identity

https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=false

Task

Your task is to print an array of size nXm with its main diagonal elements as 1's and 0's everywhere else."""


import numpy
numpy.set_printoptions(legacy="1.13")

shape = list(map(int, input().split()))
print(numpy.eye(*shape))

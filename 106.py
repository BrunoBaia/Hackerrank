"""Array Mathematics

https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=false

Task

You are given two integer arrays, a and b of dimensions nXm.
Your task is to perform the following operations:
Add ( + )
Subtract ( - )
Multiply ( * )
Integer Division ( / )
Mod ( % )
Power ( ** )"""


import numpy

n, m = input().split()
a, b = [], []
for _ in range(int(n)):
    a.append(list(map(int, input().split())))
for _ in range(int(n)):
    b.append(list(map(int, input().split())))
a, b = numpy.array(a), numpy.array(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a % b)
print(a**b)

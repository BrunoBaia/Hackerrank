"""Polar Coordinates

https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=false

Task

You are given a complex z. Your task is to convert it to polar coordinates."""


import cmath

complex_number = complex(input())
print(*cmath.polar(complex_number), sep="\n")

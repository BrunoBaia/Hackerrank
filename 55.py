"""Mod Divmod

https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=false

Task

Read in two integers,a  and b, and print three lines.
The first line is the integer division .
The second line is the result of the modulo operator .
The third line prints the divmod of a and b."""


a, b = int(input()), int(input())
res = divmod(a, b)
print(res[0],  res[1], res, sep="\n")

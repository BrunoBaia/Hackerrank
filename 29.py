"""itertools.permutations()

https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=false

Task

You are given a string s.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order."""


from itertools import permutations as pm

string, size = input().split()
for value in sorted(pm(string, int(size))):
    print("".join(value))

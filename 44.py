"""itertools.combinations_with_replacement()

https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=false

Task

You are given a string s.
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order."""


from itertools import combinations_with_replacement as cwr

string, size = input().split()
result = cwr(sorted(string), int(size))
for value in result:
    print("".join(value))

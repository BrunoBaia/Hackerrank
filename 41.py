"""itertools.combinations()

https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=false

Task

You are given a string s.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order."""


from itertools import combinations as cb

string, size = input().split()

for value in range(1, int(size)+1):
    com = cb(sorted(string), value)
    for n in com:
        print("".join(n))

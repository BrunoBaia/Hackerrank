"""Compress the String!

https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=false

Task

You are given a string s. Suppose a character 'c' occurs consecutively x times in the string.
Replace these consecutive occurrences of the character 'c' with (X, c) in the string."""


from itertools import groupby

string = input()
grouped = [(len(list(group)), int(key)) for key, group in groupby(string)]
print(*grouped)

"""Regex Substitution

https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=false

Task

You are given a text of n lines. The text contains && and || symbols.
Your task is to modify those symbols to the following: && → and, || → or"""


import re

number_of_times = int(input())
for number in range(number_of_times):
    line = input()
    line = re.sub(r"\s&&\s", " and ", line)
    line = re.sub(r"\s&&\s", " and ", line)
    line = re.sub(r"\s\|\|\s", " or ", line)
    line = re.sub(r"\s\|\|\s", " or ", line)
    print(line)

"""Group(), Groups() & Groupdict()

https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=false

Task

You are given a string s.
Your task is to find the first occurrence of an alphanumeric character in s
(read from left to right) that has consecutive repetitions."""


import re

string = input()
pattern = r"([A-Za-z0-9])(?=\1)"
result = re.search(pattern, string)
if not result:
    print(-1)
else:
    print(result.group(1))

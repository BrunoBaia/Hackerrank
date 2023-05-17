"""Incorrect Regex

https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=false

Input Format

The first line contains integer t, the number of test cases.
The next t lines contains the string s.

Output Format

Print "True" or "False" for each test case without quotes."""


import re

for _ in range(int(input())):
    pattern = input()
    try:
        test = re.compile(pattern)
        print(True)
    except re.error:
        print(False)

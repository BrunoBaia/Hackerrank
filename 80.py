"""Re.findall() & Re.finditer()

https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=false

Task

You are given a string s. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of s that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only."""


import re

pattern = r"(?<=[^aeiouAEIOU])([aeiouAEIOU]{2,})(?=[^aeiouAEIOI])"
string = input()
result = re.findall(pattern, string)
if result:
    print(*result, sep="\n")
else:
    print(-1)

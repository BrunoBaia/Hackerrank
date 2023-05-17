"""Re.start() & Re.end()

https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=false

Task

You are given a string s.
Your task is to find the indices of the start and end of string k in s."""


import re

string, string2 = input(), input()
pattern = f"{string2[0]}(?={string2[1::]})"
res = list(re.finditer(pattern, string))
if res:
    for match in res:
        print((match.start(), match.end()+len(string2)-2))
else:
    print((-1, -1))

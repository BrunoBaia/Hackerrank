"""Validating phone numbers

https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=false

Input Format

The first line contains an integer n, the number of inputs.
n lines follow, each containing some string.

Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines.
Do not print the quotes."""


import re

pattern = r"^[7-9]\d{9}$"
strings = [input() for s in range(int(input()))]
for string in strings:
    if re.match(pattern, string):
        print("YES")
    else:
        print("NO")

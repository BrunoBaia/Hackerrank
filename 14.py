"""sWAP cASE

https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=false

Input Format

A single line containing a string s.

Output Format

Convert all lowercase letters to uppercase letters and vice versa."""


def swap_case(s):
    return "".join(map(lambda x: x.lower() if x.isupper() else x.upper(), s))

"""String Validators

https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=false

Task

You are given a string s.
Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits,
lowercase and uppercase characters."""

import re

if __name__ == '__main__':
    s = input()
    alpha = bool(re.search(r"[a-zA-Z]", s))
    digit = bool(re.search(r"\d", s))

    if alpha or digit:
        print(True)
    else:
        print(False)
    print(alpha)
    print(digit)
    print(bool(re.search(r"[a-z]", s)))
    print(bool(re.search(r"[A-Z]", s)))

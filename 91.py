"""Validating UID

https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=false

Input Format

The first line contains an integer y, the number of test cases.
The next y lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines.
Do not print the quotation marks."""


import re

employees = int(input())
for number in range(employees):
    employe = "".join(sorted(input()))
    try:
        assert re.search(r"[A-Z]{2}", employe)
        assert re.search(r"\d{3}", employe)
        assert re.search(r"[A-Za-z0-9]+", employe)
        assert len(set(employe)) == 10
        print("Valid")
    except AssertionError:
        print("Invalid")

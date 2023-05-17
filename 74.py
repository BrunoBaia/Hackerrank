"""Detect Floating Point Number

https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=false

Task

You are given a string n.
Your task is to verify that n is a floating point number."""


import re

number_of_test = int(input())
pattern = r"^[\+\-]?[\.]?\d+\.?\d+$"
for number in range(number_of_test):
    test = re.search(pattern, input())
    if test is not None and test.group().count == 1:
        print(bool(test.group()))
    else:
        print(bool(test))

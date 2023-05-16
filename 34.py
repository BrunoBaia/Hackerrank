"""Exceptions

https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=false

Task

You are given two values a and b.
Perform integer division and print a//b."""


for _ in range(int(input())):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except (ZeroDivisionError, ValueError) as z:
        print(f"Error Code: {z}")

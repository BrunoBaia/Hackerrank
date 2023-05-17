"""Check Subset

https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=false

Task

You are given two sets, a and b.
Your job is to find whether set a is a subset of set b."""


for _ in range(int(input())):
    a, set_a = input(), set(input().split())
    b, set_b = input(), set(input().split())
    print(set_a.intersection(set_b) == set_a)

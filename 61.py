"""Check Strict Superset

https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=false

Task

You are given a set a and n other sets.
Your job is to find whether set a is a strict superset of each of the n sets.
Print True, if a is a strict superset of each of the n sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset."""


set_a = set(input().split())
for _ in range(int(input())):
    set_b = set(input().split())
    res = set_a.intersection(set_b)
    if res != set_b or set_a == set_b:
        print(False)
        break
else:
    print(True)

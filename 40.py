"""Symmetric Difference

https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=false

Task
Given 2 sets of integers, m and n, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either m or n but do not exist in both."""


m, set_m = input(), set(map(int, input().split()))
n, set_n = input(), set(map(int, input().split()))
result = set()
result.update(set_m.difference(set_n), set_n.difference(set_m))
print(*sorted(result), sep="\n")

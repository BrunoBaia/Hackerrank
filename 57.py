"""Maximize It!

https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=false

Input Format

The first line contains 2 space separated integers k and m.
The next k lines each contains an integer n, denoting the number of elements in the I list,
followed by n space separated integers denoting the elements in the list.

Output Format

Output a single integer denoting the value smax."""


from itertools import product

k, m = map(int, input().split())
lists = [tuple(map(lambda x: int(x)**2, input().split()[1::])) for _ in range(k)]
results = list(map(lambda x: sum(x) % m, product(*lists)))
print(max(results))

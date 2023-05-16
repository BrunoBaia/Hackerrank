"""itertools.product()

https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=false

Input Format

The first line contains the space separated elements of list a .
The second line contains the space separated elements of list b .
Both lists have no duplicate integer elements.

Output Format

Output the space separated tuples of the cartesian product."""


from itertools import product

a, b = map(int, input().split()), map(int, input().split())
print(*list(product(a, b)))

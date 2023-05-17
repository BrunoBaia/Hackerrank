"""Reduce Function

https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=false

Task

Given a list of rational numbers,find their product."""


from fractions import Fraction
from functools import reduce


def product(frac):
    t = reduce(lambda x, y: x*y, frac)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

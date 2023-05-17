"""Input()

https://www.hackerrank.com/challenges/input/problem?isFullScreen=false

Task

You are given a polynomial p of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if p(x) = k."""


x, k = input().split()
p = input()
print(eval(p.replace("x", x)) == int(k))

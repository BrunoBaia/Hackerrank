"""Polynomials

https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=false

Task

You are given the coefficients of a polynomial p.
Your task is to find the value of p at point x."""


p, x = list(map(float, input().split())), int(input())
p.reverse()
result = [p[n]*x**n for n in range(len(p))]
print(sum(result))

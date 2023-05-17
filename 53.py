"""Iterables and Iterators

https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=false

Task

You are given a list of n lowercase English letters. For a given integer k,
you can select any k indices (assume 1-based indexing) with a uniform probability from the list.
Find the probability that at least one of the k indices selected will contain the letter: 'a'."""


from itertools import combinations

size, string, length = int(input()), input().split(), int(input())
total = list(combinations(string, length))
result = sum(1 for i in total if "a" in i)/len(total)
print(result)

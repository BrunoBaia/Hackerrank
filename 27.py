"""Merge the Tools!

https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=false

Task

Split string into substrings with some rules"""


from collections import OrderedDict


def merge_the_tools(string, k):
    result = ["".join(list(OrderedDict.fromkeys(string[n:n+k]))) for n in range(0, len(string), k)]
    print(*result, sep="\n")

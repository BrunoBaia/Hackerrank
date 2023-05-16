"""Text Wrap

https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=false

Task

You are given a string s and width w.
Your task is to wrap the string into a paragraph of width w.

Returns

string: a single string with newline characters ('\n') where the breaks should be."""


import textwrap


def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    print(*wrapper.wrap(string), sep="\n")
    return ""

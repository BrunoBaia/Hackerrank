"""XML2 - Find the Maximum Depth

https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem?isFullScreen=false

Task

You are given a valid XML document, and you have to print the maximum level of nesting in it.
Take the depth of the root as 0."""


maxdepth = 0


def depth(elem, level):
    global maxdepth
    if maxdepth < level + 1:
        maxdepth = level + 1
    for child in elem:
        depth(child, level+1)

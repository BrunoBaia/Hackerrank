"""Introduction to Sets

https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=false

Task

Return the resulting float value average of unique values in a list rounded to 3 places after the decimal"""


from statistics import mean


def average(array):
    return mean(set(array))

"""Write a function

https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=false

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False

Input Format

Read n, the year to test.

Output Format

The function must return a Boolean value (True/False)."""


def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap

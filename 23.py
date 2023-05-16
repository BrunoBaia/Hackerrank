"""String Formatting

https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=false

Task

Given an integer, n, print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary"""


def print_formatted(number):
    for value in range(1, number + 1):
        lenght = len(f"{number:b}")
        print(f"{value:{lenght}} {value:{lenght}o} {value:{lenght}X} {value:{lenght}b}")

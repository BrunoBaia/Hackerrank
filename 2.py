"""Python If-Else

https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=false

Task

Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format

A single line containing a positive integer.

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird."""


def weird(number):
    if number % 2 == 1 or number in range(6, 21, 2):
        return "Weird"
    elif number in range(2, 6, 2) or number in range(20, 101, 2):
        return "Not Weird"


if __name__ == '__main__':
    n = int(input().strip())
    print(weird(n))

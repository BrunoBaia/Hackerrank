"""Print Function

https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=false

Input Format

The first line contains an integer n.

Output Format

Print the list of integers from 1 through n as a string, without spaces."""


if __name__ == '__main__':
    n = int(input())
    for number in range(n):
        print(number+1, end="")

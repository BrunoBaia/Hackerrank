"""Loops

https://www.hackerrank.com/challenges/python-loops/problem?isFullScreen=false

Input Format

The first and only line contains the integer n.

Output Format

Print n lines, one corresponding to each loop"""


n = int(input())
for number in range(0, n):
    print(number**2)

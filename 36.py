"""Time Delta

https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=false

Input Format

The first line contains T, the number of testcases.
Each testcase contains 2 lines, representing time t1 and time t2.

Output Format

Print the absolute difference t2 - t1 in seconds."""


import os
from datetime import datetime


def time_delta(t11, t22):
    ft1 = datetime.strptime(t11, "%a %d %b %Y %H:%M:%S %z")
    ft2 = datetime.strptime(t22, "%a %d %b %Y %H:%M:%S %z")
    return str(int(abs((ft1-ft2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

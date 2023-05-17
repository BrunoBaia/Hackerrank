"""Piling Up!

https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=false

Input Format

The first line contains a single integer t, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Output Format

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print Yes if it is possible to stack the cubes. Otherwise, print No.
For each test case, output a single line containing either Yes or No."""


def func(iterable):
    step = iterable.pop(0) if iterable[0] >= iterable[-1] else iterable.pop(-1)
    for _ in range(len(iterable)):
        if step >= iterable[0] >= iterable[-1]:
            step = iterable.pop(0)
        elif step >= iterable[-1] >= iterable[0]:
            step = iterable.pop(-1)
        else:
            return "No"
    return "Yes"


t = int(input())
for _ in range(t):
    n, test = input(), list(map(int, input().split()))
    print(func(test))

"""Triangle Quest

https://www.hackerrank.com/challenges/python-quest-1/problem?isFullScreen=false

Task

You are given a positive integer n. Print a numerical triangle of height n - 1."""


# More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())):
    print(sum(map(lambda x: x[0]*x[1], zip(map(lambda y: i, range(i)), map(lambda z: 10**z, range(i-1, -1, -1))))))

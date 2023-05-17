"""Map and Lambda Function

https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=false

Input Format

One line of input: an integer n.

Output Format

A list on a single line containing the cubes of the first n fibonacci numbers."""


def fibonacci(nn):
    n1, n2 = 0, 1
    fib = []
    for _ in range(nn):
        fib.append(n1)
        n1, n2 = n2, n1+n2
    return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x**3, fibonacci(n))))

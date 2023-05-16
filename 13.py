"""Tuples

https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=false

Input Format

The first line contains an integer, n, denoting the number of elements in the tuple.
The second line contains n space-separated integers describing the elements in tuple t.

Output Format

Print the result of hash(t)."""


if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))

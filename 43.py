"""Set .add()

https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=false

Task

Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her
collection. She asked for your help. You pick the stamps one by one from a stack of n country stamps.
Find the total number of distinct country stamps."""


n = int(input())
s = set()
for _ in range(n):
    s.add(input())
print(len(s))

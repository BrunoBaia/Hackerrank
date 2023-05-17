"""Collections.deque()

https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=false

Task

Perform append, pop, popleft and appendleft methods on an empty deque d."""


from collections import deque

n = int(input())
d = deque()
for number in range(n):
    name = input()
    if name.count(" "):
        name, num = name.split(" ")
        num = int(num)
    if name == "append":
        d.append(num)
    elif name == "appendleft":
        d.appendleft(num)
    elif name == "pop":
        d.pop()
    elif name == "popleft":
        d.popleft()
print(*d)

"""DefaultDict Tutorial

https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=false

Task

In this challenge, you will be given 2 integers, n and m. There are n words, which might repeat, in word group a .
There are m words belonging to word group b. For each m words, check whether the word has appeared in group a or not .
Print the indices of each occurrence of m in group a . If it does not appear, print -1 ."""


from collections import defaultdict

n, m = map(int, input().split(" "))
groupa = []
groupb = []
for _ in range(n):
    groupa.append(input())
for _ in range(m):
    groupb.append(input())

result = defaultdict(list)
for i, value in enumerate(groupa):
    result[value].append(i+1)

for value in groupb:
    if result[value]:
        print(*result[value])
    else:
        print(-1)

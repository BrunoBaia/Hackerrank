"""No Idea!

https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=false

Task

There is an array of n integers. There are also 2 disjoint sets, a and b, each containing m integers.
You like all the integers in set a and dislike all the integers in set b. Your initial happiness is 0.
For each i integer in the array, if i in a, you add 1 to your happiness. If i in b, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end."""


inp = input()
array = input().split()
seta = set(input().split())
setb = set(input().split())

result = sum(map(lambda x: 1 if x in seta else (-1 if x in setb else 0), array))

print(result)

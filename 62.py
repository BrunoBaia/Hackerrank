"""Set Mutations

https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=false

Task

You are given a set A and n number of other sets.
These n number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A."""


a, set_a = input(), set(map(int, input().split()))
for _ in range(int(input())):
    operation = input().split()
    new_set = set(map(int, input().split()))
    getattr(set_a, operation[0])(new_set)
print(sum(set_a))

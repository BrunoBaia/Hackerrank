"""Collections.namedtuple()

https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=false

Task

Your task is to calculate the average marks of the students."""


from collections import namedtuple

total, title, result = int(input()), input().split(), []
students = namedtuple('students', title)
for _ in range(total):
    student = students(*input().split())
    result.append(student)
soma = 0
for person in result:
    soma += int(person.MARKS)
print(soma/total)

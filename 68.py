"""Zipped!

https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=false

Task

The National University conducts an examination of n students in x subjects.
Your task is to compute the average scores of each student."""


from statistics import mean

n, x = input().split()
marks = []
for _ in range(int(x)):
    marks.append(list(map(float, input().split())))
for student in zip(*marks):
    print(mean(student))

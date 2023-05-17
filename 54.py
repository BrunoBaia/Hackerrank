"""Set .intersection() Operation

https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=false

Task

The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed only to French,
and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper,
one set has subscribed to the French newspaper.
Your task is to find the total number of students who have subscribed to both newspapers."""


n, english_students = input(), set(map(int, input().split()))
m, french_students = input(), set(map(int, input().split()))
print(len(french_students.intersection(english_students)))

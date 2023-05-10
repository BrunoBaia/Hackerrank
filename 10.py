"""Nested Lists

https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=false

Input Format

The first line contains an integer n, the number of students.
The 2n subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second-lowest grade.

Output Format

Print the name(s) of any student(s) having the second-lowest grade in. If there are multiple students, order their names
alphabetically and print each one on a new line."""


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: x[1])
    second_lower = []
    r = students[0][1]
    count = 0
    for value in students:
        if value[1] == r:
            count += 1
        else:
            break
    for value in range(count):
        students.pop(0)
    r = students[0][1]
    for ind, value in enumerate(students):
        if value[1] == r:
            second_lower.append(students[ind][0])
        else:
            break
    for name in sorted(second_lower):
        print(name)

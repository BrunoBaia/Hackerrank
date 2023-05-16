"""Finding the percentage

https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=false

Input Format

The first line contains the integer n, the number of students' records. The next n lines contain the names and marks
obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to
query.

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places."""


from statistics import mean

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_result = mean(student_marks[query_name])
    print(f"{query_result:.2f}")

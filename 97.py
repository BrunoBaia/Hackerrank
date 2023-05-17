"""Matrix Script

https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=false

Task

Neo has a complex matrix script. The matrix script is a X grid of strings.
It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
To decode the script, Neo needs to read each column and select only the alphanumeric characters and connect them.
Neo reads the column from top to bottom and starts reading from the leftmost column.
If there are symbols or spaces between two alphanumeric characters of the decoded script,
then Neo replaces them with a single space '' for better readability.
Neo feels that there is no need to use 'if' conditions for decoding.
Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

Input Format

The first line contains space-separated integers n (rows) and m (columns) respectively.
The next n lines contain the row elements of the matrix script.

Note: A 0 score will be awarded for using 'if' conditions in your code.

Output Format

Print the decoded matrix script."""


import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

result = zip(*matrix)
result = ["".join(i) for i in result]
result = re.sub(r"(?<=\w)[^a-zA-Z0-9]+(?=\w)", " ", "".join(result))
print(result)

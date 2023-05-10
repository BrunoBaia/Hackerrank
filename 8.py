"""List Comprehensions

https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=false

Task

Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n.

Input Format

Four integers x,y,z and n, each on a separate line.

Constraints

Print the list in lexicographic increasing order."""


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = [[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if sum([a, b, c]) != n]
    print(sorted(result))

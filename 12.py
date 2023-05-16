"""Lists

https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=false

Input Format

The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Output Format

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7
types listed above. Iterate through each command in order and perform the corresponding operation on your list.
For each command of type print, print the list on a new line."""

if __name__ == '__main__':
    N = int(input())
    lista = []
    for _ in range(N):
        i = input().split()
        if i[0] == "print":
            print(lista)
        else:
            func = getattr(lista, i.pop(0))
            i = map(int, i)
            func(*i)

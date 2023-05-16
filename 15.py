"""String Split and Join

https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=false

Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Returns

string: the resulting string

Input Format
The one line contains a string consisting of space separated words."""


def split_and_join(lines):
    return "-".join(lines.split())


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

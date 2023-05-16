"""Find a string

https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=false

Input Format

The first line of input contains the original string. The next line contains the substring.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string."""


def count_substring(string, sub_string):
    total = 0
    for s in range(len(string)-len(sub_string)+1):
        if string[s:s+len(sub_string)] == sub_string:
            total += 1
    return total

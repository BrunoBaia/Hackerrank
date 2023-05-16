"""Capitalize!

https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=false

Input Format

A single line of input containing the full name, s.

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, s."""


# Complete the solve function below.
def solve(s):
    ans = [i for i in s]
    for ind, let in enumerate(ans):
        if ind == 0 or ans[ind-1] == " ":
            ans[ind] = let.capitalize()
    return "".join(ans)

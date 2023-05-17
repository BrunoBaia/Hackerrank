"""Company Logo

https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=false

Input Format

A single line of input containing the string s.

Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order."""


from collections import Counter


if __name__ == '__main__':
    s = input()
    result = Counter(s).items()
    result = sorted(result, key=lambda x: (x[1]*-1, x[0]))
    for letter, value in result[:3:]:
        print(letter, value)

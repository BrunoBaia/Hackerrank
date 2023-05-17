"""Word Order

https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=false

Input Format

The first line contains the integer, n.
The next n lines each contain a word.

Output Format

Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.
"""


from collections import defaultdict

words = defaultdict(int)
total = int(input())
for _ in range(total):
    words[input()] += 1
print(len(words.keys()))
for word in words.values():
    print(word, end=" ")

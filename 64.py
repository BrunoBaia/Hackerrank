"""The Captain's Room

https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=false

Input Format

The first line consists of an integer, k, the size of each group.
The second line contains the unordered elements of the room number list.

Output Format

Output the Captain's room number."""


from collections import Counter

k, list_k = input(), input().split()
res = Counter(list_k)
res = sorted(res, key=res.get)
print(int(res[0]))

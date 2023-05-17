"""Triangle Quest 2

https://www.hackerrank.com/challenges/triangle-quest-2/problem?isFullScreen=false

Input Format

A single line of input containing the integer n.

Output Format

Print the palindromic triangle of size n."""


#  More than 2 lines will result in 0 score. Do not leave a blank line also
for i in range(1, int(input())+1):
    print(sum(map(lambda k: k[0]*k[1], zip([*range(1, i), i, *range(i-1, 0, -1)], map(
        lambda j: 10**j, range(len([*range(1, i), i, *range(i-1, 0, -1)])-1, -1, -1))))))

"""Find the Runner-Up Score!

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=false

Input Format

The first line contains n. The second line contains an array A of n integers each separated by a space.

Output Format

Print the runner-up score."""


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])

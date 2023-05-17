"""Any or All

https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=false

Task

You are given a space separated list of integers. If all the integers are positive,
then you need to check if any integer is a palindromic integer."""


n, list_n = input(), list(map(int, input().split()))
print(all([all([x > 0 for x in list_n]), any([str(y) == "".join(str(y)[::-1]) for y in list_n])]))

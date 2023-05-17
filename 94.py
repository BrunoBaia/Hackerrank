"""Standardize Mobile Number Using Decorators

https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=false

Input Format

The first line of input contains an integer n, the number of mobile phone numbers.
n lines follow each containing a mobile number.

Output Format

Print n mobile numbers on separate lines in the required format: +91 xxxxx xxxxx."""


def wrapper(f):
    def fun(l1):
        for ind, number in enumerate(l1):
            l1[ind] = f"+91 {number[-10:-5]} {number[-5:]}"
        f(l1)
    return fun


@wrapper
def sort_phone(lis):
    print(*sorted(lis), sep='\n')


if __name__ == '__main__':
    ll = [input() for _ in range(int(input()))]
    sort_phone(ll)

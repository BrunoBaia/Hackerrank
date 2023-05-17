"""Validating Email Addresses With a Filter

https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=false

Task

You are given an integer n followed by n email addresses.
Your task is to print a list containing only valid email addresses in lexicographical order."""


import re


def fun(s):
    pattern = r"^[\w-]+\@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$"
    res = re.match(pattern, s)
    return bool(res)


def filter_mail(mail):
    return list(filter(fun, mail))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

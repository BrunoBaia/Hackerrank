"""Validating and Parsing Email Addresses

https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=false

Input Format

The first line contains a single integer, c, denoting the number of email address.
Each line i of the n subsequent lines contains a name and an email address as two space-separated valuee,
following this format: name <user@email.com>

Output Format

Print the space-separated name and email address pairs containing valid email addresses only.
Each pair must be printed on a new line following this format: name <user@email.com>"""


import email.utils
import re

number_of_emails = int(input())
pattern = r'^[a-zA-Z][\w\-\.]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
for number in range(number_of_emails):
    mail = email.utils.parseaddr(input())
    if re.search(pattern, mail[1]):
        print(email.utils.formataddr(mail))

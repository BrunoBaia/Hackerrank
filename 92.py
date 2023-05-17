"""Validating Credit Card Numbers

https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=false

Input Format

The first line of input contains an integer n.
The next n lines contain credit card numbers.

Output Format

Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'. Do not print the quotes."""


import re

loops = int(input())
pattern = r"^[4-6]\d{3}\-?\d{4}\-?\d{4}\-?\d{4}$"
for number in range(loops):
    credit_card = input()
    check = re.search(pattern, credit_card)
    test = re.search(r"(\d)\1{3}", credit_card.replace("-", ""))
    if check is not None and test is None:
        print("Valid")
    else:
        print("Invalid")

"""Validating Postal Codes

https://www.hackerrank.com/challenges/validating-postalcode/problem?isFullScreen=false

Input Format

Locked stub code in the editor reads a single string denoting p from stdin and uses provided expression and
your regular expressions to validate if p is a valid postal code.

Output Format

You are not responsible for printing anything to stdout. Locked stub code in the editor does that."""


import re

regex_integer_in_range = r"^[1-9][0-9][0-9][0-9][0-9][0-9]$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

P = input()
print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

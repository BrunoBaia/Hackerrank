"""Validating Roman Numerals

https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=false

Task

You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True.
Otherwise, print False. Try to create a regular expression for a valid Roman numeral."""


import re

# 0 to 9
pat1 = r"(?:V?I{0,3}|IV|IX)$"
# 10 to 99
pat2 = r"(?:L?X{0,3}|XL|XC)"
# 100 to 999
pat3 = r"(?:D?C{0,3}|CD|CM)"
# 1000 to 3999
pat4 = r"M{0,3}"
regex_pattern = pat4+pat3+pat2+pat1
print(str(bool(re.match(regex_pattern, input()))))

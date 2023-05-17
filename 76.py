"""Re.split()

https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=false

Task

Your task is to complete the regex_pattern defined below, which will be used to re.split()
all of the ',' and '.' symbols in s.
It’s guaranteed that every comma and every dot in s is preceeded and followed by a digit."""


import re

regex_pattern = r"\,|\."
print("\n".join(re.split(regex_pattern, input())))

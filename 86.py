"""Hex Color Code

https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=false

Task

You are given n lines of CSS code. Your task is to print all valid Hex Color Codes,
in order of their occurrence from top to bottom."""


import re

pattern = r"(?<!^)\#[0-9a-fA-F]{3,6}"
for _ in range(int(input())):
    css = input()
    hex_color = re.findall(pattern, css)
    if hex_color:
        print(*hex_color, sep="\n")

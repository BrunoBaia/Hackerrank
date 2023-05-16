"""Find Angle MBC

https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=false

Task

You are given the lengths ab and bc.
Your task is to find MBC (angle 0, as shown in the figure) in degrees."""


import math

ab = int(input())
bc = int(input())

ang = round(math.degrees(math.atan(ab/bc)))
print(f"{ang}{chr(176)}")

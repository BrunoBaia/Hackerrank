"""Calendar Module

https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=false

Task

You are given a date. Your task is to find what the day is on that date."""


import datetime

data = input()
data = data.split(" ")
data = list(map(int, data))
data = datetime.date(data[2], data[0], data[1])
data = data.strftime("%A").upper()
print(data)

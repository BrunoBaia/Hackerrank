"""Alphabet Rangoli

https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=false

Task

You are given an integer, N. Your task is to print an alphabet rangoli of size N."""


import string


def print_rangoli(total_letters: int, reverse=True):
    letters = list(string.ascii_lowercase[0:total_letters])
    letters.reverse()
    size = total_letters * 4 - 3
    if reverse:
        loop = range(total_letters)
    else:
        loop = range(total_letters - 2, -1, -1)
    for value in loop:
        s = letters[value]
        r = letters[value::-1]
        r.pop(0)
        for letter in r:
            s = f'{letter}-{s}-{letter}'
        print(s.center(size, "-"))
    if reverse:
        print_rangoli(total_letters, reverse=False)

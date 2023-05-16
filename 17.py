"""Mutations

https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=false

Task
Read a given string, change the character at a given index and then print the modified string."""


def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    return "".join(string)

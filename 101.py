"""Default Arguments

https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=false

Task

In this challenge, the task is to debug the existing code to successfully execute all provided test files."""


class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(nnn, stream=EvenStream()):
    if type(stream) == EvenStream:
        result = [nn for nn in range(0, nnn * 2, 2)]
    else:
        result = [nn for nn in range(1, nnn * 2, 2)]
    print(*result, sep="\n")


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, stream=OddStream())

"""Designer Door Mat

https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=false

Task

Output the design pattern."""


def cone(v, h, reverse=False):
    if not reverse:
        r = range(1, v, 2)
    else:
        r = range(v-2, 0, -2)
    for i in r:
        print((i*".|.").center(h, "-"))


if __name__ == "__main__":
    n, m = map(int, input().split())
    cone(n, m)
    print("WELCOME".center(m, "-"))
    cone(n, m, reverse=True)

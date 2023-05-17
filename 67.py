"""Class 2 - Find the Torsional Angle

https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=false

Input Format

One line of input containing the space separated floating number values of the x, y and z coordinates of a point.

Output Format

Output the angle correct up to two decimal places."""


import math


class Points(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        ii = self.y * no.z - self.z * no.y
        j = -(self.x * no.z - self.z * no.x)
        k = self.x * no.y - self.y * no.x
        return Points(ii, j, k)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    xx = (b - a).cross(c - b)
    yy = (c - b).cross(d - c)
    angle = math.acos(xx.dot(yy) / (xx.absolute() * yy.absolute()))

    print("%.2f" % math.degrees(angle))

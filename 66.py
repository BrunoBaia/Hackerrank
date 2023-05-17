"""Classes: Dealing with Complex Numbers

https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem?isFullScreen=false

Task

For this challenge, you are given two complex numbers,
and you have to print the result of their addition, subtraction, multiplication, division and modulus operations."""


import math


class Complex(object):

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = self.real * no.real + self.imaginary * no.imaginary * -1
        imaginary = self.imaginary * no.real + self.real * no.imaginary
        return Complex(real, imaginary)

    def __truediv__(self, no):
        temp = Complex(no.real, -no.imaginary)
        num = self.__mul__(temp)
        den = no * temp
        return Complex(num.real / den.real, num.imaginary / den.real)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

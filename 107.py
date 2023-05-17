"""Floor, Ceil and Rint

https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=false

Task

You are given a 1-D array, A. Your task is to print the floor, ceil and rint of all the elements of A."""


import numpy

numpy.set_printoptions(legacy='1.13')
array = numpy.array(list(map(float, input().split())))
print(numpy.floor(array), numpy.ceil(array), numpy.rint(array), sep="\n")

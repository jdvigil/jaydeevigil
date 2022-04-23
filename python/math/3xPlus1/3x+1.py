#!/usr/bin/python3

import numpy

n = int(input("Please enter a number: "))
print(n)
previous_numbers = open("/mnt/c/Users/vhazo/executables/python/math/3xPlus1/used_numbers", "r").read().splitlines()

def calc_number(n):
    while n > 1:
        if numpy.mod(n, 2) == 0:
            n = numpy.floor_divide(int(n), 2)
            print(int(n))
        else:
            n = numpy.multiply(int(n), 3) + 1
            print(int(n))

if n in previous_numbers:
    if input("Number ends in 1. Do you want to see the steps? ") == "y":
        calc_number(n)
else:
    calc_number(n)

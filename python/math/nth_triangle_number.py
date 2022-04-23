#!/usr/bin/python3

import numpy

user_num = int(input("Pick a number to get it's nth triangle: "))
init_val = user_num
product = 0

if user_num <= 0:
    print("Please pick a number greater than 0")
else:
    while numpy.greater(user_num, 0):
        if product == 0:
            product = numpy.add(user_num, (numpy.subtract(user_num, 1)))
            if numpy.less(init_val, 1000000):
                print(str(user_num) + " + " + str(numpy.subtract(user_num, 1)) + " = " + str(product))
            user_num = numpy.subtract(user_num, 2)
        else:
            if numpy.less(init_val, 1000000):
                print(str(product) + " + " + str(user_num) + " = " + str(numpy.add(product,  user_num)))
            product = numpy.add(user_num, product)
            user_num = numpy.subtract(user_num, 1)

    print("The nth triangle number of " + str(init_val) + " is: " + str("{:,}".format(product)))

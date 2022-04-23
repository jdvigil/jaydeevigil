#!/usr/bin/python3

import numpy

user_num = int(input("Pick a number to get it's factorial: "))
init_val = user_num
product = 0

if user_num <= 0:
    print("Please pick a number greater than 0")
else:
    while numpy.greater(user_num, 0):
        if product == 0:
            product = numpy.multiply(user_num, (numpy.subtract(user_num, 1)))
            if len(str(init_val)) < 4:
                print(str(user_num) + " * " + str(numpy.subtract(user_num, 1)) + " = " + str(product))
            user_num = numpy.subtract(user_num, 2)
        else:
            if len(str(init_val)) < 4:
                print(str(product) + " * " + str(user_num) + " = " + str(numpy.multiply(product,  user_num)))
            product = numpy.multiply(user_num, product)
            user_num = numpy.subtract(user_num, 1)

    print("The factorial of " + str(init_val) + " is: " + str("{:,}".format(product)))

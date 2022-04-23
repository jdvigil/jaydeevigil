#!/usr/bin/python3

import numpy

pn = 2
i = numpy.subtract(pn, 1)
j = 0
print("1 is prime")

while True:
    while numpy.greater_equal(i, 0):
        if (numpy.mod(pn, i)) == 0 and (numpy.not_equal(i, 1) and numpy.not_equal(i, pn)):
            # print(str(pn) + " is not prime.")
            pn = numpy.add(pn, 1)
            i = numpy.subtract(pn, 1)
        elif numpy.equal(i, 1):
            print("" + str(pn) + " is prime" + "                                     ")
            pn = numpy.add(pn, 1)
            i = numpy.subtract(pn, 1)
        else:
            while numpy.not_equal(numpy.mod(pn, i),  0) and numpy.greater_equal(i, 1):
                i = numpy.subtract(i, 1)

                if numpy.less_equal(j, 10000):
                    print("Looking for prime numbers .\r", end="\r")
                elif numpy.greater(j, 10000) and numpy.less_equal(j, 20000):
                    print("Looking for prime numbers . .\r", end="\r")
                elif numpy.greater(j, 20000) and numpy.less_equal(j, 30000):
                    print("Looking for prime numbers . . .\r", end="\r")
                elif numpy.greater(j, 30000) and numpy.less_equal(j, 40000):
                    print("Looking for prime numbers      \r", end="\r")
                elif numpy.greater(j, 40000):
                    j = 0
                j = numpy.add(j, 1)

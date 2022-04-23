#!/usr/bin/python3

import time, numpy

pn = 2
i = pn - 1
j = 0
print("1 is prime.")

while True:
    while i >= 0:
        if pn % i == 0 and (i != 1 and i != pn):
            #print(str(pn) + " is not prime.")
            pn += 1
            i = pn - 1
        elif i == 1:
            print("                                   " + str(pn) + " is prime", end="\r")
            pn += 1
            i = pn - 1
        else:
            while pn % i != 0 and i > 1:
                i += - 1

                if j <= 10000:
                    print("Looking for prime numbers .\r", end="\r")
                elif j > 10000 and j <= 20000:
                    print("Looking for prime numbers . .\r", end="\r")
                elif j > 20000 and j <= 30000:
                    print("Looking for prime numbers . . .\r", end="\r")
                elif j > 30000 and j <= 40000:
                    print("Looking for prime numbers      \r", end="\r")
                elif j > 4000:
                    j = 0
                j += 1
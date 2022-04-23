#!/usr/bin/python3

import time

a,b = 0,1

while True:
    print(a)
    a,b = b,a+b
    time.sleep(.25)

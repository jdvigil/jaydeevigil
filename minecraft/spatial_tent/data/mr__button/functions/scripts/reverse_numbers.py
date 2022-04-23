#!/usr/bin/python3.7

file_to_open = input("Which file do you want to change the numbers of?")
open_mcfunction = open(("../" + file_to_open), "r")
read_mcfunction = open_mcfunction.read()
append_mcfunction = open(("../" + file_to_open), "a")

for i in range(0, len(read_mcfunction)):
    j = 1
    test_digits = read_mcfunction[i:i+j]
    if test_digits.isdigit() == True:
        while test_digits.isdigit() == True:
            j += 1
            test_digits = read_mcfunction[i:i+j]
        if read_mcfunction[i-1:i] == "-":
            append_mcfunction[i-1:].write("")
        else:
            append_mcfunction[i-1:].write("-")
    else:
        print(read_mcfunction)

append_mcfunction.close()

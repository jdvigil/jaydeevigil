#!/usr/bin/python3

import random, os

def pick_stick():
    prayer_list_file = open("/mnt/c/Users/vhazo/executables/python/prayer_jar/to_pray_for", "r")
    prayed_for_file = open("/mnt/c/Users/vhazo/executables/python/prayer_jar/already_prayed", "r")

    prayer_list_raw_data, already_prayed_raw_data = prayer_list_file.read(), prayed_for_file.read()
    prayer_list, already_prayed = prayer_list_raw_data.splitlines(), already_prayed_raw_data.splitlines()

    popsicle_stick = random.choice(prayer_list)

    if popsicle_stick not in already_prayed:
        with open("/mnt/c/Users/vhazo/executables/python/prayer_jar/already_prayed", "a") as ap:
            ap.write(popsicle_stick + "\n")
            print(popsicle_stick)
            ap.close()
    elif sorted(already_prayed) == sorted(prayer_list):
        print("All items have been used. Clearing file...")
        with open("already_prayed", "w") as ap:
            ap.truncate(0)
            ap.close()
        print("File cleared:. Choosing from list")
        pick_stick()
    elif popsicle_stick in already_prayed:
        prayed_for_file.close()
        pick_stick()

pick_stick()

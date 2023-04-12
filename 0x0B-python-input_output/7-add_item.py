#!/usr/bin/python3
from sys import argv
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file
""" Reads a text file and prints it to screen """


filename = "add_item.json"

if exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

for arg in argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)

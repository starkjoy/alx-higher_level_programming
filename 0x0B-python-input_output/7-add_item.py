#!/usr/bin/python3
""" Reads a text file and prints it to screen """
import importlib
from sys import argv
from os.path import exists
module_1 = importlib.import_module('5-save_to_json_file')
module_2 = importlib.import_module('6-load_from_json_file')


filename = "add_item.json"

if exists(filename):
    my_list = module_2.load_from_json_file(filename)
else:
    my_list = []

for arg in argv[1:]:
    my_list.append(arg)

module_1.save_to_json_file(my_list, filename)

#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_rev = my_list.reverse()
    for i in list_rev:
        print("{}".format(i))

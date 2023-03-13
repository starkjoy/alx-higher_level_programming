#!/usr/bin/python3
if __name__ == "__main__":
    def print_reversed_list_integer(my_list=[]):
        list_rev = my_list.reverse()
        for i in list_rev:
            print("{}".format(i))

#!/usr/bin/python3
def uppercase(str):
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            upper_c = chr(ord(c) - 32)
            print("{0}".format(upper_c), end='')
        else:
            print("{0}".format(c), end='')
    print()
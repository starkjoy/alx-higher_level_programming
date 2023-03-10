#!/usr/bin/python3
import sys
args_len = len(sys.argv)
total = 0
if __name == "__main__":
    if args_len == 1:
        print("0")
    if args_len > 1:
        for i in range(1, args_len):
            sys.argv[i] = int(sys.argv[i])
            total = total + sys.argv[i]
    print(total)

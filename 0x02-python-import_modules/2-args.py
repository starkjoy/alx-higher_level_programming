#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_len = len(sys.argv)
    if args_len == 1:
        print("0 arguments.")

    if args_len > 1:
        print("{} arguments:".format(args_len))
        for i in range(1, args_len):
            print("{}: {}".format(i, sys.argv[i]))

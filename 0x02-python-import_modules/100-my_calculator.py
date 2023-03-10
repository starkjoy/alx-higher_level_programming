#!/usr/bin/python3
import calculator_1
import sys
if __name__ = "__main__":
    args_len = len(sys.argv)
    if args_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = "+-*/"
    for i in operator:
        if i != sys.argv[2]:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    adding = '+'
    subing = '-'
    multip = '*'
    divid = '/'
    if sys.argv[2] == '+':
        print("{} {} {} = {}".format(a, adding, b, calculator_1.add(a, b)))
    if sys.argv[2] == '-':
        print("{} {} {} = {}".format(a, subing, b, calculator_1.sub(a, b)))
    if sys.argv[2] == '*':
        print("{} {} {} = {}".format(a, multip, b, calculator_1.mul(a, b)))
    if sys.argv[2] == '/':
        print("{} {} {} = {}".format(a, divid, b, calculator_1.div(a, b)))

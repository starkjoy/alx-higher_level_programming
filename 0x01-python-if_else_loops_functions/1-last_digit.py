#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number[-1]
if last_digit > 5:
    print(f"last digit of {number} is {last_digit} and is greater than 5")
if last_digit == 0:
    print(f"last digit of {number} is {last_digit} and is 0")
if last_digit < 6 and != 0:
    print(f"last digit of {number} is {last_digit} and is less than 6 and not 0")

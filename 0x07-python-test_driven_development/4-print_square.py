#!/usr/bin/python3
""" prints a square using # """


def print_square(size):
    """
    Prints a square with the character '#'

    Args:
        size: (integer) size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        print("#" * size)

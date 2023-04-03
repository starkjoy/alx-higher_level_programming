#!/usr/bin/python3
""" Adds two Integers """


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: First integer or float
        b: Second integer or float.

    Returns:
        The sum of a and b
    """

    if isinstance(a, float) or isinstance(b, float):
        return int(a) + int(b)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return a + b

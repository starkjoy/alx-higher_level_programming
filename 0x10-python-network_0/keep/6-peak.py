#!/usr/bin/python3
""" Defines a peak-finding algorithm"""

def find_peak(list_of_integers):
    """
    Actual implementation

    Args:
        list_of_integers: list of integers
    """

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    else:
        for i in range(1, size - 1):
            if list_of_integers[i - 1] < list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[i]
        return None

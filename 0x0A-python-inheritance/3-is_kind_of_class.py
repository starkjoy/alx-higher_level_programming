#!/usr/bin/python3
""" Returns True if object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    checks if it is an instance of an inherited class
    obj: object
    a_class: class
    return: true or false for case where object is instance of class
    """
    return isinstance(obj, a_class)

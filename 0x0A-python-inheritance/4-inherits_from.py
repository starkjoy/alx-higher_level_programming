#!/usr/bin/python3
""" Returns True if object is an instance of a class """


def inherits_from(obj, a_class):
    """
    checks if it is an instance of an inherited class
    obj: object
    a_class: class
    return: true or false for case where object is instance of class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

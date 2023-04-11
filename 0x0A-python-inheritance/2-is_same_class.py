#!/usr/bin/python3
""" Returns True if object is an instance """


def is_same_class(obj, a_class):
    """ 
    checks if it is an instance of the class
    obj: object
    a_class: class
    return: true or false for case of object being an instance of class
    """
    return type(obj) ==  a_class

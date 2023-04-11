#!/usr/bin/python3
""" Returns instances and methods of an object """


def lookup(obj):
    """ returns list of attributes and methods of an object
    obj: object
    """
    return dir(obj)

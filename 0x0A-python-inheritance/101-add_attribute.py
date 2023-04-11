#!/usr/bin/python3
""" adds a new attribute """


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible
    Args:
        obj (object): The object to add
        attr (str): The name of the attribute
        value (any): The value of the attribute to add
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

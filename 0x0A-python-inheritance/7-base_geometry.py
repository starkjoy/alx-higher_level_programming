#!/usr/bin/python3
""" creates an empty class """


class BaseGeometry:
    """ empty class """
    def __init__(self):
        """ initializes BaseGeometry"""
        pass

    def area(self):
        """ area with exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ value validator """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

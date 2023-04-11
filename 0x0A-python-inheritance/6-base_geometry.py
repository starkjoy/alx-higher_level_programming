#!/usr/bin/python3
""" creates an empty class """


class BaseGeometry:
    """ empty class """
    def __init__(self):
        """ initializes BaseGeometry """
        pass

    def area(self):
        """ returns area with exception """
        raise Exception("area() is not implemented")

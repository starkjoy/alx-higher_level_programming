#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """ Creates a rectangle """

    def __init__(self, width=0, height=0):
        """ initializes rectangle object

        Args:
            width (int): rectangle width
            height (int): rectangle height
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

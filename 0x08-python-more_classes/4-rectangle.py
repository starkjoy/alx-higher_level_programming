#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """ Creates a rectangle """

    def __init__(self, width=0, height=0):
        """ initializes rectangle object """
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
            raise TyperError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ returns rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """ string representation of rectangle """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.height):
                rectangle_str += "#" * self.width
                if i != self.height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        """ string representation to rebuild rectangle object """
        return f"Rectangle({self.width}, {self.height})"

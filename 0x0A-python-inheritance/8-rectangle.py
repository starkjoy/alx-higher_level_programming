#/usr/bin/python3
""" creates a sub-class """


class Rectangle(BaseGeometry):
    """ sub-class of BaseGeometry"""

    def __init__(self, width, height):
        """ initializes Rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

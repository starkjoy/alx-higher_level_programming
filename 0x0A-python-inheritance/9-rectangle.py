#/usr/bin/python3
""" creates a sub-class """


class Rectangle(BaseGeometry):
    """ sub-class of BaseGeometry"""

    def __init__(self, width, height):
        """ initializes rectangle """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self, width, height):
        """ returns area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ string representation of the Rectangle """
        return "[Rectangle] {} / {}".format(self.__width, self.__height)

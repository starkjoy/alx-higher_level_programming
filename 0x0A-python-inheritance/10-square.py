#/usr/bin/python3
""" creates a sub-class """


class Square(Rectangle):
    """ sub-class of Rectangle"""

    def __init__(self, size):
        """ initializes square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns area of square """
        return self.__size * self.__size

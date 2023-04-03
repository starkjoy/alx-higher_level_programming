#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """ Creates a rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initializes rectangle object """
        type(self).number_of_instances += 1
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
        rect = []
        for  i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
                return ("".join(rect))

    def __repr__(self):
        """ returns a string representation to rebuild object """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ deleted rectangle instance """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

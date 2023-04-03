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
                rectangle_str += print_symbol * self.width
                if i != self.height - 1:
                    rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        """ returns a string representation to rebuild object """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ deleted rectangle instance """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns bigger rectangle based on area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif area(rect_1) == area(rect_2):
            return rect_1
        elif area(rect_1) > area(rect_2):
            return rect_1
        elif area(rect_1) < area(rect_2):
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ returns a new rectangle instance width == height == size 

        Args:
            size: size of square

        """
        return (cls(size, size))

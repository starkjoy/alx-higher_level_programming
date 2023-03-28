#!/usr/bin/python3
'''Creates a Square object'''


class Square:
    '''Square Class'''

    def __init__(self, size=0):
        ''' Makes Square

        Args: size: size of square '''

        self.__size = size

    @property
    def size(self):
        ''' gets/ sets size of square '''

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' Returns area '''

        return self.__size * self.__size

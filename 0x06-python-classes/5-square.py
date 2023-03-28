#!/usr/bin/python3
'''Creates Square object'''


class Square:
    ''' Square Class '''

    def __init__(self, size=0):
        ''' Makes Square Class

        Args: size: size of class '''

        self.__size = size

    @property
    def size(self):
        ''' gets size of square '''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        ''' finds area '''
        return self.__size * self.__size

    def my_print(self):
        ''' prints square '''
        if self.__size == 0:
            print()
        else:
            for in range(self.__size):
                print('#' * self.__size)

#!/usr/bin/python3
'''Creates a Square object'''


class Square:
    ''' Square Class '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Makes Square

        Args: size: size of square position: position of square'''
        self.size = size
        self.position = position

    @property
    def size(self):
        ''' sets or gets size of square '''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    @property
    def position(self):
        ''' sets/gets the position of square '''
        return self.__position

    @position.setter
    def position(self, value):
        if not isintance(value, tuple) or len(value) !=2 or not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        ''' Returns Area of square '''
        return self.__size * self.__size

    def my_print(self):
        ''' prints square '''
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

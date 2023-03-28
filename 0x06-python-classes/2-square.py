#!/usr/bin/python3
'''This is a Square class'''


class Square:
    ''' Square Class '''

    def __init__(self, size=0):
        ''' Makes a square

        Args: size: size of square
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

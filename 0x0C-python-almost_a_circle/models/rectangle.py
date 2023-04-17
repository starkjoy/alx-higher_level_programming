#!/usr/bin/python3
""" Rectangle class """


from models.base import Base


class Rectangle(Base):
    """ creates a rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes rectangle class """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        """ gets width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width """
        return self.__width = value

    @property
    def height(self):
        """ gets height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height """
        return self.__height = value

    @property
    def x(self):
        """ gets x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets x """
        return self.__x = value

    @property
    def y(self):
        """ gets y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y """
        return self.__y = value

    def area(self):
        """ returns area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints the rectangle instance with the character '#'"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ overrides str method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args:
            self.id, self.width, self.height, self.x, self.y = args
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a rectangle """
        dict_rect = {'id': self.id, 'width': self.width, 'height': self.height,
                     'x': self.x, 'y': self.y}
        return dict_rect

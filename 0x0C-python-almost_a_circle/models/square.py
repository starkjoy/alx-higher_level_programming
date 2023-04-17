#!/usr/bin/python3
""" Square class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ creates a square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes square class """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ overrides str method """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """ Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter method for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns arguments to each attribute """
        if args:
            self.id, self.size, self.x, self.y = args
            self.width = self.size
            self.height = self.size
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == "size":
                    self.width = value
                    self.height = value

    def to_dictionary(self):
        """ dictionary representation of square """
        dict_sqr = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dict_sqr

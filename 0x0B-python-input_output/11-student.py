#!/usr/bin/python3
""" A student class """


class Student:
    """ Student Class """

    first_name: str
    last_name: str
    age: int

    def __init__(self, first_name: str, last_name: str, age: int):
        """ initializes Student Class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dictionary representation of Student instance
        Args:
            attrs: class attributes
        """
        if attrs is None:
            return self.__dict__
        else:
            dict_serials = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    dict_serials[key] = value
            return dict_serials

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance
        Args:
            json: source dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)

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

    def to_json(self):
        """ retrieves dictionary representation of Student instance """
        class_dict = self.__dict__
        dict_serials = {}
        for key, value in class_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                dict_serials[key] = value
        return dict_serials

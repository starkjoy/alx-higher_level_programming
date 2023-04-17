#!/usr/bin/python3
""" creates a class called base """


import json

class Base:
    """ creates a base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the base class """
        if id is not None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ parses to json string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json to file """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="UTF-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """ parsed from json string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates instances of class """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ loads from file """
        filename = cls.__name__ + ".json"
        list_Obj = []
        with open(filename, "r", encoding="UTF-8") as f:
            json_string = f.read()
            if not json_string:
                return list_Obj
            else:
                obj_list = cls.from_json_string(json_string)
                for obj_dict in obj_list:
                    obj_instance = cls.create(**obj_dict)
                    list_Obj.append(obj_instance)
            return list_Obj

#!/usr/bin/python3
import json
""" returns dictionary description with simple data structure """


def class_to_json(obj):
    """  dictionary to python data structure
    Args:
        obj: class instance
    """
    class_dict = obj.__dict__
    serializable_dict = {}
    for key, value in class_dict.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value
    return serializable_dict

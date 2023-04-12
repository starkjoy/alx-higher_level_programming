#!/usr/bin/python3
import json
""" returns json representation of object """


def to_json_string(my_obj):
    """ 
    json generator
    Args:
        my_obj: object for conversion
    """
    return json.dumps(my_obj)

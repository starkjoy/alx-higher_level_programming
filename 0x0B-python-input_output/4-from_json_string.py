#!/usr/bin/python3
""" returns python object representation of json string """
import json


def from_json_string(my_str):
    """
    json to python object
    Args:
        my_str: string for deserialization
    """
    return json.loads(my_str)

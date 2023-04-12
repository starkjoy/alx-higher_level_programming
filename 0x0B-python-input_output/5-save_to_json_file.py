#!/usr/bin/python3
import json
""" Writes json object to text file """


def save_to_json_file(my_obj, filename):
    """ 
    Writes json object to file
    Args:
        filename: file
        my_obj: json object
    """
    with open(filename, "w", encoding="UTF8") as files:
        json.dump(my_obj, files)

#!/usr/bin/python3
""" creates an object from a json file """
import json


def load_from_json_file(filename):
    """
    creates an object from a json file
    Args:
        filename: file
    """
    with open(filename, "r", encoding="UTF8") as files:
        obj = json.load(files)
        return obj

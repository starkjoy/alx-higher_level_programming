#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not value:
        return a_dictionary
    else:
        for key, valuee in a_dictionary.items():
            if valuee == value: 
                del a_dictionary[key]
    return a_dictionary

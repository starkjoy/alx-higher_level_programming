#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for key, valuee in a_dictionary.items():
            if valuee == value: 
                del a_dictionary[key]
                break
    return a_dictionary

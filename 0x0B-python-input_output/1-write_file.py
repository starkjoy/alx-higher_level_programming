#!/usr/bin/python3
""" Writes to a file and returns the number of characters """


def write_file(filename="", text=""):
    """ 
    Writes to and return character count of file
    Args:
        filename: file
        text: data to wriet to file
    """
    with open(filename,"w",  encoding="UTF8") as files:
        files.write(text)
    char_count = len(text)
    return char_count


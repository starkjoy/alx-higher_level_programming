#!/usr/bin/python3
""" Reads a text file and prints it to screen """


def read_file(filename=""):
    """ 
    Reads a file and prints it
    Args:
        filename: file
    """
    with open(filename, encoding="UTF8") as files:
        file_read = files.read()
        print(file_read)

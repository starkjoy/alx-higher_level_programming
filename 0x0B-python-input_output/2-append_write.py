#!/usr/bin/python3
""" Appends string to file """


def append_write(filename="", text=""):
    """ 
    appends string to file
    Args:
        filename: file
        text: data to append to file
    """
    with open(filename, "a", encoding="UTF8") as files:
        char_prev = files.tell()
        files.write(text)
        char_now = files.tell()
    return char_now - char_prev

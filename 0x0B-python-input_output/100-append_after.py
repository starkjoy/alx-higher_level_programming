#!/usr/bin/python3
""" Reads a text file and adds a line if search string is found """


def append_after(filename="", search_string="", new_string=""):
    """
    Reads, search and append
    Args:
        filename: file to read and append
        search_string: string to find
        new_string: string to append
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)

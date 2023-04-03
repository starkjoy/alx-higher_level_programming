#!/usr/bin/python3
""" Prints a text with 2 new lines after some characters """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters '.?:'

    Args:
        text: (string) text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuation = [".", "?", ":"]
    new_string = ""
    for letter in text:
        new_string = new_string + letter
        if letter in punctuation:
            print(new_string.strip())
            new_string = ""
    print(new_string,end="")

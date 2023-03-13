#!/usr/bin/python3
def no_c(my_string):
    filtered_chars = []
    for char in my_string:
        if char not in {'c', 'C'}:
            filtered_chars.append(char)
    return ''.join(filtered_chars)

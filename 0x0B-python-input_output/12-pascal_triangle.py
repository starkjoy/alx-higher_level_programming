#!/usr/bin/python3
""" Implements pascals triangle """


def pascal_triangle(n):
    """
    Returns a list of lists of integers of pascals triangle
    Args:
        n: number of rows for pascals triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_index in range(1, n):
        row = [1]
        for j in range(1, row_index):
            value = (row[j - 1] * (row_index - j + 1)) // j
            row.append(value)
        row.append(1)
        triangle.append(row)
    return triangle

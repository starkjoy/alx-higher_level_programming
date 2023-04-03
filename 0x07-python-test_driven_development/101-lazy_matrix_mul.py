#!/usr/bin/python3
""" multiplies two matrices using numpy """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Finds the product of two matrices

    Args:
        m_a: First matrix
        m_b: Second matrix
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list)for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) or not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a should contain only integers or floats and m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size and each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    mat_pro = np.dot(m_a, m_b)
    print(mat_pro)

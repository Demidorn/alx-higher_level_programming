#!/usr/bin/python3
"""Divides each element of a matrix of numbers by a number"""


def matrix_divided(matrix, div):
    """
    Check if matrix is a list of lists of integers or
    floats
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rows = []
    for row in matrix:
        len_rows.append(len(row))
    if not all(elem == len_rows[0] for elem in len_rows):
        raise TypeError("Each row of the matrix must have the same size")
	"""Check if div is a number (integer or float) and not equal to 0"""

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
	"""
        Divides each element in the matrix by div and round
        to 2 decimal places
	"""

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix

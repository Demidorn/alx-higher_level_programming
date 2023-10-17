#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        result = [num ** 2 for num in row]
        new_matrix.append(result)
    return new_matrix

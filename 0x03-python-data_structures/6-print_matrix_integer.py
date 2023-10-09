#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in range(len(matrix)):
        j = len(matrix[element])
        for i in range(j):
            if i != j - 1:
                new_char = ' '
            else:
                new_char = ''
            print("{:d}".format(matrix[element][i]), end=new_char)
        print("")
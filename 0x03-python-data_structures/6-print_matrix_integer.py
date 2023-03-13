#!/usr/bin/python3

"""A function that prints a matrix of integers.
    By: Gold Israel

    Args:
        matrix: The matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = '\t'.join(str(element)for element in row)
        print("{}".format(row_str))

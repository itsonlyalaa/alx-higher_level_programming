#!/usr/bin/python3
"""a module to divide"""


def matrix_divided(matrix, div):
    """a function to divide all the elements in a list"""
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(error)

    if type(matrix) is not list:
        raise TypeError(error)

    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(error)
        for item in lists:
            if type(item) is not int and type(item) is not float:
                raise TypeError(error)

    for lists in matrix:
        if len(lists) == 0:
            raise TypeError(error)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if not all(len(lists) == len(matrix[0]) for lists in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in lists] for lists in matrix]

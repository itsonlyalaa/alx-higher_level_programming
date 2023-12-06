#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for items in matrix:
        new_matrix.append([number ** 2 for number in items])
    return new_matrix

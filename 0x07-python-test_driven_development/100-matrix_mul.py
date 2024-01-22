#!/usr/bin/python3
"""This module has a function that multiplies two matrix"""


def matrix_mul(m_a, m_b):
    """a function that multiplies two matrix"""

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    num_colum = 0
    num_row = 0

    if m_a == []:
        raise ValueError("m_a can't be empty")

    for row in m_a:
        if type(row) != list:
            raise TypeError("m_a must be a list of lists")

        lens = len(m_a[0])

        if row == []:
            raise ValueError("m_a can't be empty")

        if lens != len(row):
            raise TypeError("each row of m_a must be of the same size")

        num_colum = len(row)

        for coln in row:
            if type(coln) != int and type(coln) != float:
                raise TypeError("m_a should contain only integers or floats")

    if m_b == []:
        raise ValueError("m_b can't be empty")

    for row2 in m_b:
        if type(row2) != list:
            raise TypeError("m_b must be a list of lists")

        lens2 = len(m_b[0])
        if row2 == []:
            raise ValueError("m_b can't be empty")

        if lens2 != len(row2):
            raise TypeError("each row of m_b must be of the same size")

        num_row += 1
        for column2 in row2:
            if type(column2) != int and type(column2) != float:
                raise TypeError("m_b should contain only integers or floats")

    if num_colum != num_row:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for row_1 in m_a:
        x = 0
        x_row = []
        while x < len(m_b[0]):
            result = 0
            y = 0
            for column_1 in row_1:
                result += column_1 * m_b[y][x]
                y += 1
            x_row.append(result)
            x += 1
        mul_matrix.append(x_row)

    return mul_matrix

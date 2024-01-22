#!/usr/bin/python3
"""a module to print square of hashes"""


def print_square(size):
    """a function to print square of hashes"""
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        j = 0
        for j in range(0, size):
            print("#", end="")
        print()

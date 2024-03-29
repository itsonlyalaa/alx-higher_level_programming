#!/usr/bin/python3
"""python module"""


class Square:
    """define a square class"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the square area"""
        area = self.__size * self.__size
        return area

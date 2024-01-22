#!/usr/bin/python3
"""python square module"""


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

    def __eq__(self, other):
        """define comaparsion of equals to"""
        return self.area() == other.area()

    def __ne__(self, other):
        """define comaparsion of not equal to"""
        return self.area() != other.area()

    def __lt__(self, other):
        """define comaparsion of less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """define comaparsion of less than or equal to"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """define comaparsion of greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """define comaparsion of greater than or equals to"""
        return self.area() >= other.area()

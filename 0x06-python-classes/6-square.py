#!/usr/bin/python3
"""Square module"""


class Square:
    """Class defined for square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """__size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """__position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError('position must be a tuple of ' +
                                '2 positive integers')
        self.__position = value

    def area(self):
        """Calulates area of square."""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Prints text representation of square"""
        if self.__size == 0:
            print()
        else:
            for vOfset in range(0, self.__position[1]):
                print()
            for row in range(0, self.__size):
                for hOfset in range(0, self.__position[0]):
                    print(" ", end="")
                for coln in range(0, self.__size):
                    print("#", end="")
                print()

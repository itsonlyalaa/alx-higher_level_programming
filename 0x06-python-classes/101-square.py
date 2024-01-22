#!/usr/bin/python3
"""Square module"""


class Square:
    """Class defined for square generation"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """size getter"""
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
        """position getter"""
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
        """Calulates area of square"""
        area = self.__size * self.__size
        return area

    def str_format(self):
        """formats text representation of square"""
        str = ''
        if self.__size == 0:
            str += '\n'
        else:
            for vOffset in range(0, self.__position[1]):
                str += '\n'
            for row in range(0, self.__size):
                for hOffset in range(0, self.__position[0]):
                    str += ' '
                for coln in range(0, self.__size):
                    str += '#'
                str += '\n'
        return str

    def my_print(self):
        """Prints text representation of square"""
        print(self.str_format(), end="")

    def __str__(self):
        """Returns: self.str_format() minus trailing newline"""
        length = len(self.str_format())
        truncated = self.str_format()[:length - 1]
        return truncated

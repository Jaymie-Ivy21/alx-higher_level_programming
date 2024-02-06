#!/usr/bin/python3

"""a class Square that defines a square by size"""

class Square:

    """method of the square size"""

    def __init__(self, size=0):
        """args:
        __size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """method of the area of the square"""

    def area(self):
        return self.__size**2


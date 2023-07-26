#!/usr/bin/python3

"""Defining a class"""


class Square:

    def __init__(self, size=0):
        """Initializing the class square
        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """method to get the area of square"""
        return self.__size * self.__size

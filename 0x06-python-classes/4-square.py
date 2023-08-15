#!/usr/bin/python3

"""Defining the class"""


class Square:

    def __init__(self, size=0):
        """Initializing the class"""
        self.__size = size

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value of the size
        Args:
            value: value of the size
        Raise:
            TypeError: if the size is not an integer
            ValueError: if the size is > 
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size


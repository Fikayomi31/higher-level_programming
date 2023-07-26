#!/usr/bin/python3

"""Defining the class"""


class Square:

    def __init__(self, size=0):
        """Initializing class square
        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

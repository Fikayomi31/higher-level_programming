#!/usr/bin/python3

"""Defining the class"""


class Square:

    def __init__(self, size=0):
        """Initializing the class"""
        self.__size = size

    @property
    def size(self):
        """Return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting the value of the size
        Args:
            value: value of the size
        Raise:
            TypeError: if size is not an integer
            ValueError: if size is <
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)

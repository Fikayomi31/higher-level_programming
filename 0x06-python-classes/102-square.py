#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """Representation of the class square"""

    def __init__(self, size=0):
        """Initialization of the class square
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value for the size
        Args:
            value: value for the size
        RaiseError:
            ValueError: if size is < 0
            TypeError: if size is not a number
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current area of the square"""
        return self.__size * self.__size

    def __eq__(self, other):
        """for == comparision"""
        return self.area() == other.area()

    def __ne__(self, other):
        """for != comparision"""
        return self.area() != other.area()

    def __lt__(self, other):
        """for < comparision"""
        return self.area() < other.area()

    def __le__(self, other):
        """for <= comparision"""
        return  self.area() <= other.area()

    def __gt__(self, other):
        """for > comparision"""
        return self.area() > other.area()

    def __ge__(self, other):
        """for >= comparision"""
        return self.area() >= other.area()

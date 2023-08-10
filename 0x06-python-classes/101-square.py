#!/usr/bin/python3
"""Defining a class"""


class Square:

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the class
        Args:
            size: size of the square
            position: position of the square
        """
        self.size = size
        self.position = position

    def size(self):
        """

#!/usr/bin/python3

"""Defining  the class"""


class Square:

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setting the size
        Args:
            value: value of the the size
        Raise:
            TypeError: if size is not integer
            ValueError: if size is < 
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setting the value of the position
        Args:
            value: value of the position
        Raise:
            TypeError: if position is not tuple of 2 integer
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive interger")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            # check if the tuple is int and >= 0
            raise TypeError("position must be a tuple of 2 positive interger")
        self.__position = value

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print stdout the square #"""
        my_square = ""
        if self.__size == 0:
            return
        else:
            for i in range(self.__position[1]):
                my_square = "\n" #print empty line
            for i in range(self.__size):
                my_square += " " * self.__position[0] + "#" * self.__size + "\n"
            return my_square

    def __str__(self):
        """str representation"""
        return self.my_print()

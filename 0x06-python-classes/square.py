#!/usr/bin/python3

class Square:

    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    @property
    def height(self):
        print("Retrieving the height")

        return self.__height

    @height.setter
    def height(self, value):
        
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter number for height")

    @property
    def width(self):
        print("Retrieving the width")

        return self.__width
    
    @width.setter
    def width(self, value):
        
        if value.isdigit():
            self.__width = value
        else:
            print('Please only enter number for width')

    def area(self):
        return int(self.__width) * int(self.__height)



x = Square()
height = input("Enter height value : ")
width = input("Enter width value : ")
x.height = height
x.width = width

print("Height :", x.height)
print("Width :", x.width)

print("The Area is :", x.area())

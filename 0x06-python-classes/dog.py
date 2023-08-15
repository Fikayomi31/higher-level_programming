#!/usr/bin/python3

"""Defining the class"""
class Dog:

    def __init__(self, name="", height=0, weight=0):
        """initiazing the class"""
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


spot = Dog("Spot", 66, 26)
spot.eat()
spot.run()
spot.bark()

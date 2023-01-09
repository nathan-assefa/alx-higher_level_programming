#!/usr/bin/python3
"""Creating a new empty class, but in this case
it is going to have a method called area
"""


class BaseGeometry:
    """defing a method area"""
    def area(self):
        raise Exception("area() is not implemented")

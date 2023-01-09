#!/usr/bin/python3
"""Creating a new class, but in this case
it is going to have a method called area
"""


class BaseGeometry:
    """defing a method area"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.name = name
        self.value = value

#!/usr/bin/python3
"""The new class Rectangle inherits from the old
class BaseGeometry
"""


class Rectangle(BaseGeometry):
    """Rectangle class inherits from the parent class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

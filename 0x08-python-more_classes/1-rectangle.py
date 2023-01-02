#!/usr/bin/python3
"""defining a class"""


class Rectangle:

    """Initializing a new object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """Getting width attribute"""
    @property
    def width(self):
        return self.__width

    """Setting widht attribute"""
    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    """getting height attribute"""
    @property
    def height(self):
        return self.__height

    """setting height attribute"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

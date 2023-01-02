#!/usr/bin/python3
"""defining a class"""


class Rectangle:

    """public class attributes"""
    number_of_instances = 0

    """public class attributes and
    be any type
    """
    print_symbol = '#'

    """Initializing a new object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """str method to print user friendly string"""
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ''
        hash_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                hash_str += Rectangle.print_symbol
            if i != self.__height - 1:
                hash_str += '\n'
        return hash_str

    """___repr__ method to return a string that can be parsed"""
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """Dleting an rectangle object"""
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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
        self.__width = value

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
        self.__height = value

    """Defining method for aread"""
    def area(self):
        return self.__width * self.__height

    """Defining method for perimeter"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

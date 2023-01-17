#!/usr/bin/python3
"""The Base class is the parent class of
the class Rectangle, and the Rectangle class
inherits the methods and attributs of the Base
class using super() method
Args:
    width: width of a structure
    height: height of a structure
    x, and y are the two paramets detrmines the
    the extra features of the structure.
    id: This attribute is from the parent class and
    its vaue is detirmined by its state.
There are also different methods in this Class used to
set up a structure.
"""
from models.base import Base


class Rectangle(Base):
    """intializing a new instance using init method"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """str method to print an object when print is used"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height
                )

    def validation(self, key, val):
        """This function validats the data"""
        if type(val) != int:
            raise TypeError("{} must be an integer".format(key))
        if (key == "width" or key == "height") and val <= 0:
            raise ValueError("{} must be an integer".format(key))
        if (key == "x" or key == "y") and val < 0:
            raise ValueError("{} must be >= 0".format(key))

    @property
    def width(self):
        """Getting width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting a value to width attribure"""
        self.validation("width", value)
        self.__width = value

    @property
    def height(self):
        """Getting height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting a value for height attribute"""
        self.validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Getting x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting a value for x attribute"""
        self.validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Getting y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting a value for y attribute"""
        self.validation("y", value)
        self.__y = value

    def area(self):
        """Area method to find the area"""
        return self.__width * self.__height

    def display(self):
        """To display the structure"""
        if self.__y > 0:
            [print() for i in range(self.__y)]
        for i in range(self.__height):
            [print(" ", end="") for k in range(self.__x)]
            [print("#", end="") for j in range(self.__width)]
            print()

    def update(self, *args, **kwargs):
        """This function is used to intialize the attributes
        of a new instance. When this function is called, then
        the attributes of a new instance would be intialized
        """
        if args:
            """This is for the new non key parametrs"""
            x = 0
            for arg in args:
                if x == 0:
                    if arg is not None:
                        self.id = arg
                elif x == 1:
                    self.width = arg
                elif x == 2:
                    self.height = arg
                elif x == 3:
                    self.x = arg
                elif x == 4:
                    self.y = arg
                x += 1
        elif kwargs and len(kwargs) != 0:
            """This is for key worded parametrs"""
            for key, value in kwargs.items():
                if key == "id":
                    if value is not None:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """To convert to dictionary"""
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width,
                }

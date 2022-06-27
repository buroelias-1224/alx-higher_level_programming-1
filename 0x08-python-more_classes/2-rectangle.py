#!/usr/bin/python3
"""
    Define a Rectangle class with width and height
"""


class Rectangle:
    """Representation of a Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize a rectnagle
        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Set/get value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Set/get value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns area of a rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__width + self.__height))

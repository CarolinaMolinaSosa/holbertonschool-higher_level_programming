#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)
"""


class Rectangle:
    """ Empty class Reactangle"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    """ Width """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        """ if width is less than 0 """
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Height """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ height must be an integer """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        """ if height is less than 0 """
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Public instance method """
    def area(self):
        return self.__width * self.__height

    """ Public instance method """
    def perimeter(self):
        """ if width or height is equal to 0, perimeter is equal to 0 """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    """ Print rectangle """
    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ''
        for i in range(self.__height-1):
            print('#' * self.__width)
        print('#' * self.__width, end="")
        return ''

    """Return string representation of the rectangle """
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    """ Bye rectangle... """
    def __del__(self):
        print("Bye rectangle...")

#!/usr/bin/python3
""" Defines a rectangle"""

class Rectangle:
    """ defined by instance of height and width"""
    def __init__(self, width=0, height=0):
        """ initializes rectangle instance
            Args:
            width = width of a rectangle
            heigth = heigth of a rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """ generates a string representation"""
        if self._width == 0 or self._height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self._height):
                for j in range(self._width):
                    rectangle_str += "#"
                if i < self._height - 1:
                    rectangle_str += "\n"
            return rectangle_str
    def __repr__(self):
        """Return a string representation of a Rectangle instance
            that is able to recreate a new instance by using eval()
        """
        return f"Rectangle({self._width}, {self._height})"

    @property
    def width(self):
        """ retrieves the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """ sets width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """retrieves height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """ sets height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """ calculates area of a rectangle instance by
        returning width * height """
        return self._width * self._height

    def perimeter(self):
        """ calculates perimeter of a rectangle
        given by 2*(height + width """
        if self._height == 0 or self._width == 0:
            return 0
        return 2 * (self._width + self._height)

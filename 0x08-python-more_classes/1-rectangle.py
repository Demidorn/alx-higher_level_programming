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



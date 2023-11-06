#!/usr/bin/python3
"""
new class rectangle that inherites
instances fron BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ initialized variables"""
    def __init__(self, width, height):
        """initialization"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """ returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns <width/height>"""
        a = str(self.__width)
        b = str(self.__height)
        return "[Rectangle]" + a + "/" + b

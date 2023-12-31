#!/usr/bin/python3
""" declaration of class square that
inherits from class rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square inherits from rectangle class """

    def __init__(self, size):
        """ initializes square """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns area of square """
        return super().area()

    def __str__(self):
        """ returns [Square] <width>/<height> string """
        a = str(self.__size)
        return "[Square] " + a + "/" + a

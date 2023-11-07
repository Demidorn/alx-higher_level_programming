#!/usr/bin/python3
""" class square inherits from rectangle class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square inherits from rectangle class """

    def __init__(self, size):
        """ initializes square """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

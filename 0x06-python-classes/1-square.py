#!/usr/bin/python3

""" this class define a square"""


class Square:
    """Private instance attribute and instantation with optional
    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Constructor method to initialize a Square instance.
    """

    def __init__(self, size = 0):
        """Initialize a Square instance."""
            self.__size = size 

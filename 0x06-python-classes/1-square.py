#!/usr/bin/python3

""" this class define a square"""


class Square:
    """Private instance attribute and instantation with optional
    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size): Constructor method to initialize a Square instance.
    """

    def __init__(self, size=0):
         """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

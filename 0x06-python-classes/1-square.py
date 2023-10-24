#!/usr/bin/python3
"""class Square"""


class Square:
    """Private instance attribute and instantation with optional"""
    def __init__(self, size=0):
        if type(size) is not int:
             """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The size of the square.
        """
            self.__size = size

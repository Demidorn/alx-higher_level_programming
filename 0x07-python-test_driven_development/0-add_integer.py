#!/usr/bin/python3
""" Adds two integers together"""

def add_integer(a, b=98):
    """Returns the addition of a and b,
    or an error if a and b are not integers or floats
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    """Calculate the sum and return it as an integer"""
    result = int(a) + int(b)
    return result

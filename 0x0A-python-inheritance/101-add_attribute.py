#!/usr/bin/python3
"""
add attribute if possible
or raise TypeError
"""


def add_attribute(obj, name, value):
    """
    check if obj is instance of non built in class"""
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

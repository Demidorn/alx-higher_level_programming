#!/usr/bin/python3
"""
function checks for instance nature of the object
if it's the exact specified instance, it return
true otherwise returns false
"""


def is_same_class(obj, a_class):
    """ checking if instance is as specified"""
    return type(obj) is a_class

#!/usr/bin/python3

"""
function returns true if it inherited instances from
a class directly or indirectly otherwise returns false
"""
def inherits_from(obj, a_class):
    if type(obj) != a_class):
        return isinstance(obj, a_class)
    return False

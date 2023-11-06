#!/usr/bin/python3
""" defines base class BaseGeometry"""


class BaseGeometry:
    """ sub class function"""
    def area(self):
        """ raises exception error"""
        raise Exception("area() is not implemented")
    """ a Public instance method that validates the value"""
    def integer_validator(self, name, value):
        """
        validate value
        """
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

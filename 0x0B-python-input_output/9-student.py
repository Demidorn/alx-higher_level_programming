#!/usr/bin/python3
"""
definesstudent class with new instatiation
described by;
    first_name
    last_name
    age
"""


class Student:
    """ initialization """
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """ retrieves a dictionary representation """
        return self.__dict__

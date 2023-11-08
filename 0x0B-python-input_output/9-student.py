#!/usr/bin/python3
"""
definesstudent class with new instatiation
described by;
    first_name
    last_name
    age
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """ initialization of student obj """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation """
        return self.__dict__

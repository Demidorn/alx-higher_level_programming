#!/usr/bin/python3
""" new class that inherites its attributes from list class"""


class MyList(list):
    """ initialization of function that prints
    all atributes inherited from the list base class
    """

    def print_sorted(self):
        """variable to sort list in ascending order"""
        new_list = sorted(self)
        print(new_list)

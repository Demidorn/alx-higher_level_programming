#!/usr/bin/python3

"""
class MyInt
inherits from int

"""


class MyInt(int):
    def __eq__(self, other):
        """
        equal to
        """
        return False

    def __ne__(self, other):
        """
        not equal to
        """
        return True

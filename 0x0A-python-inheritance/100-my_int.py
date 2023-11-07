#!/usr/bin/python3
"""
new class Myint
"""


class MyInt(int):
    def __eq__(self, other):
        """ equal to"""
        return super().__ne__(other)

    def __ne__(self, other):
        """not equal to"""
        return super().__eq__(other)

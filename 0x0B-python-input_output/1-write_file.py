#!/usr/bin/python3
""" a function that writes a string to a text file
and returns number of characters written """


def write_file(filename="", text=""):
    """ read file """
    with open(filename, 'w', encoding='utf-8') as f:
        xters = f.write(text)
        return xters

#!/usr/bin/python3
""" a function that writes a string to a text file
and returns number of characters written """


def write_file(filename="", text=""):
    """ read file """
    with open(filename, 'r', encoding='utf-8') as f:
        z = 0
        for file in f:
            z += 1
        return z

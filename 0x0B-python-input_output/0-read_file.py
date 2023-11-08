#!/usr/bin/python3
""" function that reads text file
and prints to stdout """


def read_file(filename=""):
    """ read file """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")

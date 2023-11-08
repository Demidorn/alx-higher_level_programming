#!/usr/bin/python3
""" this function appends a string at the
end of the text file and returns the  number
of characters added """


def append_write(filename="", text=""):
    """ adds string of characters """
    with open(filename, 'a', encoding='utf-8') as f:
        xters = f.write(text)
        return xters

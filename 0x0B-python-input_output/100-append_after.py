#!/usr/bin/python3
"""
function inserts a line of file to a text file
prototype:def append_after(filename="", search_string="", new_string="")
"""


def append_after(filename="", search_string="", new_string=""):
    """ append a string into a new_line after find another """
    text = ""
    with open(filename, mode="r", encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        if line.find(search_string) != -1:
            text += line + new_string
        else:
            text += line
    with open(filename, mode="w", encoding='utf-8') as f:
        f.write(text)

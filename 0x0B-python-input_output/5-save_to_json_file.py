#!/usr/bin/python3
"""
function that writes an Object to a text file
using json representation

prototype: def save_to_json_file(my_obj, filename)
"""
import json


def save_to_json_file(my_obj, filename):
    """ json representation that writes an object """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

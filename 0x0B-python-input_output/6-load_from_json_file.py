#!/usr/bin/python3
"""
 function that creates an Object from a “JSON file”
 prototype: def load_from_json_file(filename)
 """
import json


def load_from_json_file(filename):
    """ json representation of an object """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

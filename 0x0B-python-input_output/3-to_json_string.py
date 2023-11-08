#!/usr/bin/python3
""" function that returns JSON  representation
of an object

prototype: def to_json_string(my_obj) """


import json


def to_json_string(my_obj):
    return json.dumps(my_obj)

#!/usr/bin/python3
"""
function that returns an object represented
by a json string

prototype: def from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    return json.loads(my_str)

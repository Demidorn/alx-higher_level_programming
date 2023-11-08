#!/usr/bin/python3
"""
function that returns dictionary description
with simple data structure
prototype: def class_to_json(obj)
"""


def class_to_json(obj):
    if not hasattr(obj, '__dict__'):
        raise ValueError("Object is not serializable")

    serializable_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict

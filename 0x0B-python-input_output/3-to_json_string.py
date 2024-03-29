#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """to_json_string  returns the JSON representation of an object (string)
    Args:
        my_obj (obj): any object for example list, dict
    """
    return json.dumps(my_obj)

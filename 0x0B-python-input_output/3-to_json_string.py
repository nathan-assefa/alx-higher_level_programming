#!/usr/bin/python3
"""This function returns the JSON representation
of a python file
"""
import json


def to_json_string(my_obj):
    """Returning JSON file"""
    return json.dumps(my_obj)

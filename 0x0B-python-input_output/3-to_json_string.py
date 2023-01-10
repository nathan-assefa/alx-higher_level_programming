#!/usr/bin/python3
"""This function returns the JSON representation
of a python file
"""
import json


def to_json_string(my_obj):
        return json.dump(my_obj)

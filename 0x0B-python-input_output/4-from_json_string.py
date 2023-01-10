#!/usr/bin/python3
"""This function returns python data structure
form json file
"""
import json


def from_json_string(my_str):
    """Retuns python data structure"""
    return json.loads(my_str)

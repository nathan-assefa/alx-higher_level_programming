#!/usr/bin/python3
"""Writing to json file from python object
using json.dump method
"""
import json


def save_to_json_file(my_obj, filename):
    """form python object ot json file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

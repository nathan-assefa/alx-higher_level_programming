#!/usr/bin/python3
"""This function creates a python object from
the json file
"""
import json


def load_from_json_file(filename):
    """From json file to python object"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

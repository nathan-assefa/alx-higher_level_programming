#!/usr/bin/python3
"""This function creates a python object from
the json file
"""
import json


def load_from_json_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.loads(file)

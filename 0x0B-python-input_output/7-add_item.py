#!/usr/bin/python3
"""This functioin adds arguments to python list
and write them into the json file
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
import sys


try:
    jsonList = load_from_json_file('add_item.json')
except:
    jsonList = []

save_to_json_file(jsonList.append(argv[:]))

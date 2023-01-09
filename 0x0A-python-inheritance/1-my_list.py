#!/usr/bin/python3
"""This function inheret every functionality
from the list object. In addition to the list
functionality, this function has also its own
methos calld print_sorted to print the sorted
lists
"""

class MuList(list):
    """this method print a sorted list"""
    def print_sorted(self):
        print(sorted(self))

#!/usr/bin/python3
"""This function appends to a file and counts
the number of charachters that appends to the
file
"""


def append_write(filename="", text=""):
    """Appending and counting the charachters"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)

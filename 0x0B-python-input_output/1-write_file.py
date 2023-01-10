#!/usr/bin/python3
"""This function writes to the file and at the same
time counts the number of charchter it writes to the
file
"""


def write_file(filename="", text=""):
    """writing and counting the charachters"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)

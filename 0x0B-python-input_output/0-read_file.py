#!/usr/bin/python3
"""This function reads from a file and prints
the content to stdout
"""


def read_file(filename=""):
    """open fucntion opens the file in read mode"""
    with open('filename') as file:
        print("{}".format(file.read()), end="")

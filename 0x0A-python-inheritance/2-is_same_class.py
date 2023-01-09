#!/usr/bin/python3
"""Returns True if and only if the object is
an instance of a specified class
"""


def is_same_class(obj, a_class):
    """obj is an instance that inherets from
    a_class
    """
    return type(obj) is a_class

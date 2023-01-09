#!/usr/bin/python3
"""Retuns true if if an object(obj) is an instance of
a clss a_class
"""


def inherits_from(obj, a_class):
    """Returns True of Flase depednig on the object type"""
    return False if type(obj) is a_class else isinstance(obj, a_class)

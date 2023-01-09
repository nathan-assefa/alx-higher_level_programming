#!/usr/bin/python3
"""Write a function that returns True if the object
is an instance of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Returns True of Flase depednig on the object type"""
    return False if type(obj) is a_class else isinstance(obj, a_class)

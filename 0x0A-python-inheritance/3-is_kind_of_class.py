#!/usr/bin/python3
"""This function returns True if and onlu if
the an object is an instance of a supper or base
class. Otherwise this function returns false
"""
def is_kind_of_class(obj, a_class):
    """obj is an object that inherits from
    a_class, and this function checks if obj_j
    exactely inherits from a_class
    """
    if isinstance(obj, a_class):
        return True
    return False

#!/usr/bin/python3
"""this function is to add new attribute to an
object if possible. if not possible, the functoin
raises an exception
"""


def add_attribute(obj, attribute, value):
    """to add new atributes to an object"""
    print(obj)
    if isinstance(obj, type):
        raise TypeError("[TypeError] can't add new attribute")
    print(id(obj))
    obj.attribute = value

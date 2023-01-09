#!/usr/bin/python3
"""This class inherits from list class and
invert some of the functionalities of list
"""


class MyInt(int):
    """To inverst somem methods of list class"""
   
    def __eq__(self, a):
        return False
    def __ne__(self, a):
        return True

#!/bin/usr/python3

"""This function prints the full name, and the
first parameter is the first name of a person and
the second parameteris the last name of a person
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

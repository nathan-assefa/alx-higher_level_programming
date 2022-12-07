#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for dic in a_dictionary:
        if dic == key:
            a_dictionary[dic] = value
    a_dictionary[key] = value
    return a_dictionary

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = {}
    for dic in a_dictionary:
        new_dic[dic] = a_dictionary[dic]
        result = new_dic[dic]
        new_dic[dic] = result*2
    return new_dic

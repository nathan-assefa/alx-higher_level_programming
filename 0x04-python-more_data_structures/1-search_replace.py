#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    new_list = list()
    for r in my_list:
        if r != search:
            new_list.append(r)
            i += 1
        else:
            new_list.append(replace)
    return new_list

#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_new = list()
    for st1 in set_1:
        for st2 in set_2:
            if st1 == st2:
                set_new.append(st2)
    return set_new

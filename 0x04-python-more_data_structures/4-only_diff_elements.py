#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    inSet1 = set_1 - set_2
    inSet2 = set_2 - set_1
    new_set = inSet1.union(inSet2)
    return new_set

#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    new_set = list()
    for st1 in set_1:
        for st2 in set_2:
            if st1 != st2:
                new_set.append(st1)
                new_set.append(st2)
    return set(new_set)

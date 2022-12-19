#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    my_list = [number for number in my_list if isinstance(number, int)]
    i = 0
    try:
        for num in my_list[:x]:
            print(num, end="")
            i += 1
        print()
        return i
    except IndexError:
        print("list index out of range")

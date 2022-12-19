#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    my_list = [number for number in my_list if isinstance(number, int)]
    i = 0

    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
            i += 1
        except IndexError:
            break
    print()
    return i

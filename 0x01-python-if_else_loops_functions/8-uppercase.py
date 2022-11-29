#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if ord(upper) >= ord('a') and ord(upper) <= ord('z'):
            print("{}".format(chr(ord(upper) - 32)), end="")
        else:
            print("{}".format(chr(ord(upper))), end="")
    print()

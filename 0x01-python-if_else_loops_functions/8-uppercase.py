#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if ord(upper) >= ord('a') and ord(upper) <= ord('z'):
            upper = format(chr(ord(upper) - 32))
        print("{}".format(upper), end="")
    print()

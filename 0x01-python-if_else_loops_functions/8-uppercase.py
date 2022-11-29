#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if ord(upper) in range(ord('a'), ord('z')):
            print("{}".format(chr(ord(upper) - 32)), end="")
        else:
            print(chr(ord(upper)), end="")
    print()

#!/usr/bin/env python3
# islower = __import__('7-islower').islower

def islower(c):
    for lower in range(ord("a"), ord("z") + 1):
        if (c == chr(lower)):
            return (True)
    return (False)

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))

#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') + 1):
    if (chr(alpha) != 'q' and chr(alpha) != 'e'):
        print("{}".format(chr(alpha)), end="")

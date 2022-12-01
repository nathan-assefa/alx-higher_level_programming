#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        print("{} {}:".format(len(argv) - 1, "argument"))
        print("{}: {}".format(len(argv) - 1, argv[1]))
    elif len(argv) == 1:
        print("{} {}.".format(len(argv) - 1, "arguments"))
    else:
        print("{} {}:".format(len(argv) - 1, "arguments"))

        i = 1
        while (i < len(argv)):
            print("{}: {}".format(i, argv[i]))
            i += 1

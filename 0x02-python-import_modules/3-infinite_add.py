#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    _sum = 0;
    i = 1
    while (i < len(argv)):
        _sum += int(argv[i])
        i += 1

    print("{}".format(_sum))

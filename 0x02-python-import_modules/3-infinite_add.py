#!/usr/bin/python3
from sys import argv

i = 1
def main():
    if len(argv) != 1:
        while (i < len(argv)):
            print("{}".format(int(argv[i])))
            i += 1
if __name__ == "__main__":
    main()

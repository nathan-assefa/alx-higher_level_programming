#!/usr/bin/python3
from sys import argv

from sys import argv

a = int(argv[1])
b = int(argv[2])

def main():
    print("{}".format(add(a, b)))

def add(a, b):
    return (a + b)
if __name__ == "__main__":
    main()

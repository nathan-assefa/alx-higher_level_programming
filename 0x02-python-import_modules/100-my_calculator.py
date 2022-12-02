#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

operator = {"+": add, "-": sub, "*": mul, "/": div}

if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], operator[argv[2]](a, b)))


#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return (fct(*args))
    except Exception as d:
        print("Exception: {}".format(d), file=sys.stderr)
        return (None)

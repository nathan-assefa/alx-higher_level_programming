#!usr/bin/python3
def safe_print_integer(value):
    try:
        val = int(value)
        print("{}".format(val))
        return True
    except ValueError:
        return False

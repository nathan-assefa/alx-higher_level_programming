#!/usr/bin/python3

"""Print_square function print square of hashtag
symbol. The paramter size is the dimention whereby
the function builds the square
"""


def print_square(size):
    """prints # size times"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    import doctest
    doctest.testmod()

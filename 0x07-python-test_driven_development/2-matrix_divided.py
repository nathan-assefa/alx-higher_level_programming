#!/usr/bin/python3

"""This function divides each memebers of the list
by the div, and there are certain conditions that
affects the operations. The parameter matrix is the
has to be list of lists and the parameter div shoud be
either integer or float
"""


def matrix_divided(matrix, div):
    if not type(matrix) == list or not all(
            isinstance(ty, list) for ty in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    size_list = 0
    for _list in matrix:
        if size_list == 0:
            size_list = len(_list)
        elif size_list != len(_list):
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(j, (int, float)) for j in _list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in _list] for _list in matrix]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

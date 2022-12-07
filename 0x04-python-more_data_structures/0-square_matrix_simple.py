#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_list = list()
    for i in range(len(matrix)):
        new_list[i] = list(map(lambda x: x**2, matrix[i]))
    return new_list

#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_list = list()
    for i in range(len(matrix)):
        new_matrix = list(map(lambda x: x**2, matrix[i]))
        new_list.append(new_matrix)
    return new_list

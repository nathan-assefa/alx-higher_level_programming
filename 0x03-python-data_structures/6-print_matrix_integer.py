#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print('')
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[j][j], end=" ")
            print()

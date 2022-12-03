#!/usr/bin/python3
if __name__ = "__main__":
    def print_matrix_integer(matrix=[[]]):
        if len(matrix) == 1:
            print('')
        else:
            for i in range(len(matrix)):
                for j in range(len(matrix)):
                    print(matrix[i][j], end=" ")
                print()

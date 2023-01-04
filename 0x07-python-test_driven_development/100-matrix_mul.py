#!/usr/bin/python3
"""This function returns the product of two
matrixes. The two parameters m_a and m_a are
the two matrixes the is going to be multiplied
by the the function
"""


def matrix_mul(m_a, m_b):
    """Multiplying two integers and the two parameters
    are matrixes, and the number of column of m_a should
    be equal to m_b to perform the operation
    """

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    size = 0
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if size == 0:
            size = len(row)
        elif size != len(row):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if size == 0:
            size = len(row)
        elif size != len(row):
            raise TypeError("each row of m_b must be of the same size")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not all(isinstance(val, (float, int)) for val in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(val, (float, int)) for val in row):
            raise TypeError("m_b should contain only integers or floats")
    matrix = []
    for i in range(len(m_a)):
        _list = []
        for j in range(len(m_b[0])):
            item = 0
            for k in range(len(m_b)):
                item += m_a[i][k] * m_b[k][j]
            _list.append(item)
        matrix.append(_list)
    return matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod()

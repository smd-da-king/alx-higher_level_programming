#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ret = []
    for row in matrix:
        nR = list(map(lambda x: x * x, row))
        ret.append(nR)
    return ret

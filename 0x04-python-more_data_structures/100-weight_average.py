#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    res, weight = 0, 0
    for elem in my_list:
        res += elem[0] * elem[1]
        weight += elem[1]
    return res / weight

#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum1 = 0
    for num in set(my_list):
        sum1 += num
    return sum1

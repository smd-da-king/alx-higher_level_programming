#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    maxN = my_list[0]
    for n in my_list[1:]:
        if n > maxN:
            maxN = n
    return maxN

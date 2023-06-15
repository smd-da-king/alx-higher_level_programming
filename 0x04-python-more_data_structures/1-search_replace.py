#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newLst = list(map(lambda x: x, my_list))
    for i in range(len(newLst)):
        newLst[i] = replace if newLst[i] == search else newLst[i]
    return newLst

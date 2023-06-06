#!/usr/bin/python3
for x in range(0, 9):
    for y in range(x, 10):
        if x == 8 and y == 9:
            break
        if x != y:
            print("{}{}".format(x, y), end=", ")
print("89")

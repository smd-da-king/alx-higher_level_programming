#!/usr/bin/python3
def print_last_digit(number):
    lastDg = abs(number) % 10
    print("{}".format(lastDg), end="")
    return (lastDg)

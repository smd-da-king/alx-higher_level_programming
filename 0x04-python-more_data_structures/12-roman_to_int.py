#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    num, j = 0, len(roman_string) - 1
    while j >= 0:
        if roman_string[j] == 'I':
            if (j+1 < len(roman_string) and
               (roman_string[j+1] == 'V' or roman_string[j+1] == 'X')):
                num -= 1
            else:
                num += 1
        elif roman_string[j] == 'V':
            num += 5
        elif roman_string[j] == 'X':
            if (j+1 < len(roman_string) and
               (roman_string[j+1] == 'L' or roman_string[j+1] == 'C')):
                num -= 10
            else:
                num += 10
        elif roman_string[j] == 'L':
            num += 50
        elif roman_string[j] == 'C':
            if (j+1 < len(roman_string) and
               (roman_string[j+1] == 'D' or roman_string[j+1] == 'M')):
                num -= 100
            else:
                num += 100
        elif roman_string[j] == 'D':
            num += 500
        elif roman_string[j] == 'M':
            num += 1000
        j -= 1
    return num

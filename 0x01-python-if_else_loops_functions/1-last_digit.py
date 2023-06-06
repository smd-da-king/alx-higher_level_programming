#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstD = abs(number) % 10

print(f"Last digit of {number} is", end=" ")

if lstD > 5 and number > 0:
    print(f"{lstD} and is greater than 5")
elif lstD == 0:
    print(f"{lstD} and is 0")
else:
    if number < 0:
        print("-", end="")
    print(f"{lstD} and is less than 6 and not 0")

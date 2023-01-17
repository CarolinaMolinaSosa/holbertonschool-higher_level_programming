#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_d = abs(number) % 10
print(f"Last digit of {number} is", end=" ")
if number < 0:
    print(f"{l_d * -1} and is less than 6 and not 0")
elif l_d > 0 and l_d < 6:
    print(f"{l_d} and is less than 6 and not 0")
elif l_d > 5:
    print(f"{l_d} and is greater than 5")
else:
    print(f"{l_d} and is 0")

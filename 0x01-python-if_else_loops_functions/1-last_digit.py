#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
conditions = ""
if last_digit > 5:
    conditions = "greater than 5"
elif last_digit < 6 and last_digit != 0:
    conditions = "less than 6 and not 0"
else:
    conditions = "0"
print(f"Last digit of {number:d} is {last_digit:d} and is {conditions}")

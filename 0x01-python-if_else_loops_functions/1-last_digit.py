#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
if int(last_digit) > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif int(last_digit) == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
elif 0 < int(last_digit) < 6:
    print("Last digit of", number, "is", last_digit, "and is less
            than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_dig = str(number)[-1]
f_dig = str(number)[0]
n_neg = f_dig + l_dig

if int(l_dig) > 5 and number > 0:
    print("Last digit of", number, "is", l_dig, "and is greater than 5")

elif int(l_dig) == 0:
    print("Last digit of", number, "is", l_dig, "and is 0")

elif int(l_dig) < 6 and number > 0:
    print("Last digit of", number, "is", l_dig, "and is less than 6 and not 0")

else:
    print("Last digit of", number, "is", n_neg, "and is less than 6 and not 0")

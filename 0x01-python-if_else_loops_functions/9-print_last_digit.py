#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = number * -1
    val = number % 10
    print(val, end="")
    return val

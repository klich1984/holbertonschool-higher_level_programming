#!/usr/bin/python3
def uppercase(str):
    for i in str:
        val = ord(i)
        if val >= 97 and val <= 122:
            val = chr(val - 32)
        else:
            val = chr(val)
        print("{:s}".format(val), end="")
    print("")

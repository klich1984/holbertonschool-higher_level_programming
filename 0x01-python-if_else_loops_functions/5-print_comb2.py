#!/usr/bin/python3
for alp in range(100):
    if alp < 99:
        print("{:02}".format(alp), end=", ")
    else:
        print("{}".format(alp))

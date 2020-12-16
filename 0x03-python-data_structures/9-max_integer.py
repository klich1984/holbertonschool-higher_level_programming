#!/usr/bin/python3
def max_integer(my_list=[]):
    leng = len(my_list)
    if my_list:
        Max = my_list[0]
        for i in range(leng):
            if (my_list[i] > Max):
                Max = my_list[i]
        return Max
    else:
        return "None"

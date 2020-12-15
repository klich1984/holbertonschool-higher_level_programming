#!/usr/bin/python3
def no_c(my_string):
    new_list = list(my_string)
    for i in range(len(my_string)):
        if new_list[i] == 'c' or new_list[i] == 'C':
            new_list[i] = ""

    return "".join(new_list)

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len_list = 0
    for i in my_list:
        len_list += 1
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
    except IndexError:
        print()
        return len_list

    return x

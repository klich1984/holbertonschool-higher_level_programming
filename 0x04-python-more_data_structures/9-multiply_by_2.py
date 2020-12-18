#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    liste = sorted(a_dictionary.keys())
    for item in liste:
        new_dict[item] = a_dictionary[item] * 2
    return new_dict

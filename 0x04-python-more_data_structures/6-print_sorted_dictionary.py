#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    liste = (sorted(list(a_dictionary.keys())))
    for key in liste:
        print("{:}: {:}".format(key, a_dictionary[key]))

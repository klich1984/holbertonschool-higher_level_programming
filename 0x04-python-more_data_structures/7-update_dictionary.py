#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dictionary = {key: value}
    a_dictionary.update(new_dictionary)
    return a_dictionary

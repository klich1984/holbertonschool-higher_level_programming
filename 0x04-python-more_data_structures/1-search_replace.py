#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = my_list[:]
    for i in range(len(new_matrix)):
        if search == new_matrix[i]:
            new_matrix[i] = replace
    return new_matrix

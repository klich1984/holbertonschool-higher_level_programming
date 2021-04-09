#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """This function finds a peak in a list of integers.

    Args:
        list_of_integers (list): list of unsorted integers
    """
    print('lista = ', list_of_integers)
    if len(list_of_integers) == 0:
        return None
    else :
        list_of_integers.sort()
        print('lista ordenada = ', list_of_integers)
        print("ultimo dogito = ", list_of_integers[-1])
        print('max number = ', max(list_of_integers))

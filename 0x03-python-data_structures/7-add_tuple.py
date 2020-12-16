#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l1 = list(tuple_a) + [0, 0]
    l2 = list(tuple_b) + [0, 0]
    l3 = [l1[0] + l2[0]] + [l1[1] + l2[1]]
    return tuple(l3)

#!/usr/bin/python3

"""A function that retrieves an element from a list like in c
   by: Gold Israel
"""


def element_at(my_list, idx):
    if idx < 0:
        return None

    elif idx >= len(my_list):
        return None

    else:
        return my_list[idx]

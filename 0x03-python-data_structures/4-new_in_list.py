#!/usr/bin/python3

""" A function that replaces an element in a list at a specific position
        without modifying the original list
    By: Gold Israel

    Args:
       my_list: The list
       idx: Variable containing Index of the element to be replaced
        element: The new element to replace the old element with

    Return:
        Returns the new list.
"""


def new_in_list(my_list, idx, element):
    lst = my_list
    my_list[idx] = element

    if idx < 0:
        return lst

    elif idx >= len(my_list):
        return lst

    else:
        return my_list

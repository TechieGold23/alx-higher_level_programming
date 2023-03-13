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
    new_list = my_list.copy()
    if idx < 0:
        return my_list.copy()

    elif idx > len(new_list) - 1:
        return my_list.copy()

    else:
        new_list[idx] = element
        return new_list

#!/usr/bin/python3

""" A function that replaces an element of a list at a specific position
   By; Gold Israel

   Args:
       my_list: A list of elements
       idx: An integer representig the index of the element to be replaced
       element: The new element to replace the old element with.


   Returns:
       The new list.
 """


def replace_in_list(my_list, idx, element):

    lst = my_list

    if idx < 0:
        return lst

    elif idx >= len(my_list):
        return lst

    else:
        my_list[idx] = element
        return my_list


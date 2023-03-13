#!/usr/bin/python3

"""A function that removes all occurrences of a chracter from a string,
    both upper and lower.

    By: Gold Israel

    Args:
        my_string: The string to remove the character from

    Return:
        Returns the moddified strig with the character removed
"""


def no_c(my_string):
    new_string = ""

    for char in my_string:
        if char not in ['c', 'C']:
            new_string += char
    return new_string

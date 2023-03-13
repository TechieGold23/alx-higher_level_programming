#!/usr/bin/python3

"""A function that prints all integers of a list in reverse order
   By: Gold Israel


   Args:
       my_list: A list of integers


    Return:
         Returns reversed list.
"""


def print_reversed_list_integer(my_list=[]):
    rev_list = my_list[::-1]
    for i in rev_list:
        print("{:d}".format(my_list[i - 1]))

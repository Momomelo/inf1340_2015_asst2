#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    sub_length = len(substring)
    for i in range (start, end):
        check = input_string[i: i+sub_length]
        if (check == substring):
            return i
    return -1


def multi_find(input_string, substring, start, end):
    """
    Describe your function

    :param :
    :return:
    :raises:

    """
    result = ""
    for i in range (start, end):
        index_found = find(input_string, substring, start, end)
        if (index_found == -1):
            break
        else:
            result = result + str(index_found) + ","
            start = index_found + len(substring)
    return result[0:len(result)-1]

print(multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20))
print(find("Ni! Ni! Ni! Ni!", "Ni", 4, 20))
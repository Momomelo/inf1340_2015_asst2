#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

This module converts performs substring matching for DNA sequencing

"""

__author__ = "Kei'ichiro Yamamoto, Albert Tai"
__email__ = "keiichiro.yamamoto@mail.utoronto.ca , albert.tai@mail.utoronto.ca"
__copyright__ = "2015 Kei'ichiro Yamamoto, Albert Tai"
__license__ = "MIT License"


def find(input_string, substring, start, end):
    """
    This returns the lowest index where the substring is found in the index
    range from beginning position to end position. If it is not found we
    will return -1.

    :param input_string: the string that is being looked in (String)
    :param substring: the string that we are trying to find
    :param start: the position we are starting to look at in the input string (Integer)
    :param end: the position we are end looking for the string (Integer)
    :return: starting position of the string or -1 if cannot be found (Integer)

    """
    # storing the length of the string trying to find
    sub_length = len(substring)
    # cycle through the entire string being checked for substring
    for i in range (start, end):
        # check is a string that is from current position to substring position
        check = input_string[i: i+sub_length]
        # check if the substring and string potential are same
        if (check == substring):
            # if so return position
            return i
    # otherwise return -1 
    return -1


def multi_find(input_string, substring, start, end):
    """
    This returns the all the index where the substring is found in the index
    range from beginning position to end position. If it is not found we
    will return no information.

    :param input_string: the string that is being looked in (String)
    :param substring: the string that we are trying to find
    :param start: the position we are starting to look at in the input string (Integer)
    :param end: the position we are end looking for the string (Integer)
    :return: all the positions found in this format (pos1, pos2, pos3...)  (String
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

#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

def is_equal(table1, table2):
    if (len(table1[0]) == len(table2[0])):
        for i in range(0, len(table1[0])):
            if(table1[0][i] != table2[0][i]):
                return False
        return True
    else:
        return False

def union(table1, table2):
    """
    Perform the union set operation on tables, table1 and table2.

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    table_union = []
    # checking if schema is true to calculate rest'=
    if is_equal(table1,table2):
        # concatenate the two tables together
        table_union = table1 + table2
        # removing duplicates of the concentated table
        table_union= remove_duplicates(table_union)
    # if schema does not match just throw an exception
    else:
        raise MismatchedAttributesException('Schema of tables do not match')
    return table_union


def intersection(table1, table2):
    """
    Describe your function

    """
    table_intersect = []
    if is_equal(table1, table2):
        # clean the tables to ensure all uniqueness
        table1 = remove_duplicates(table1)
        table2 = remove_duplicates(table2)

        for i in range(0, len(table1)):
            for j in range(0, len(table2)):
                if(table1[i][0] == table2[j][0]):
                    similar_count = 1
                    for k in range(1, len(table1[0])):
                        if(table1[i][k] == table2[j][k]):
                            similar_count=similar_count+1
                        else:
                            break
                    if (similar_count == len(table1[0])):
                        table_intersect.append(table1[i])
                        break
    #if schema does not match just throw an exception
    else:
        raise MismatchedAttributesException('Schema of tables do not match')
    return table_intersect


def difference(table1, table2):
    """
    Describe your function

    """
    return []


#####################
# HELPER FUNCTIONS ##
#####################
def remove_duplicates(l):
    """
    Removes duplicates from l, where l is a List of Lists.
    :param l: a List
    """

    d = {}
    result = []
    for row in l:
        if tuple(row) not in d:
            result.append(row)
            d[tuple(row)] = True

    return result


class MismatchedAttributesException(Exception):
    """
    Raised when attempting set operations with tables that
    don't have the same attributes.
    """
    pass

grad = [['Number', 'Surname', 'Age'], [7274, 'Robinson', 37], [7432, "O'Malley", 39], [9824, 'Darkes', 38],[1337, 'Batman', 22]]
gradcheck = [['Number', 'Surname', 'Age'], [8862, 'Robinson', 37], [7522, "O'Malley", 39], [1337, 'Batman', 22], [9824, 'Darkes', 38], [1142, 'Albert', 22]]
print(is_equal(grad, gradcheck))
tablefun = union(grad, gradcheck)
print(tablefun)

tablewhy = remove_duplicates(grad + gradcheck)
print(tablewhy)

tableintersect = intersection(grad, gradcheck)
print(tableintersect)
#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

This module performs table operations on database tables
implemented as lists of lists.

"""

__author__ = "Kei'ichiro Yamamoto, Albert Tai"
__email__ = "keiichiro.yamamoto@mail.utoronto.ca , albert.tai@mail.utoronto.ca"
__copyright__ = "2015 Kei'ichiro Yamamoto, Albert Tai"
__license__ = "MIT License"


def is_equal(table1, table2):
    """
    This is a helper function that tests if table 1 is same format/attributes (column wise)
    as table 2 in the same order

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: boolean value whether it is same or not
    """
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
    if is_equal(table1, table2):
        # concatenate the two tables together
        table_union = table1 + table2
        # removing duplicates of the concentated table
        table_union = remove_duplicates(table_union)
    # if schema does not match just throw an exception
    else:
        raise MismatchedAttributesException('Schema of tables do not match')
    return table_union


def intersection(table1, table2):
    """
    Perform the intersection operation on tables, table 1 and 2

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    table_intersect = []
    # checking if attributes of two tables are same
    if is_equal(table1, table2):
        # clean the tables to ensure all uniqueness
        table1 = remove_duplicates(table1)
        table2 = remove_duplicates(table2)
        # going through row by row of table 1
        for i in range(0, len(table1)):
            # going through row by row of table 2
            for j in range(0, len(table2)):
                # checking if first item in row is same in both
                if(table1[i][0] == table2[j][0]):
                    # if so start a counter of similarities
                    similar_count = 1
                    # check every item in that row if same as other
                    for k in range(1, len(table1[0])):

                        if(table1[i][k] == table2[j][k]):
                            similar_count = similar_count+1
                        else:
                            break
                    if (similar_count == len(table1[0])):
                        table_intersect.append(table1[i])
                        break
    # if schema does not match just throw an exception
    else:
        raise MismatchedAttributesException('Schema of tables do not match')
    return table_intersect


def difference(table1, table2):
    """
    Perform the difference operation on tables, table 1 and 2, returns the rows that are on table 1
    but not on table 2

    :param table1: a table (a List of Lists)
    :param table2: a table (a List of Lists)
    :return: the resulting table
    :raises: MismatchedAttributesException:
        if tables t1 and t2 don't have the same attributes
    """
    table_difference = table1[:]
    table_intersection = intersection(table1, table2)
    # checking if attributes of two tables are same
    if is_equal(table1, table2):
        table1 = remove_duplicates(table1)
        for i in range(0, len(table_intersection)):
            for j in range(1, len(table_difference)):
                # checking if first item in row is same in both
                if(table_intersection[i][0] == table_difference[j][0]):
                    # if so start a counter of similarities
                    similar_count = 1
                    # check every item in that row if same as other
                    for k in range(1, len(table1[0])):
                        if(table_intersection[i][k] == table_difference[j][k]):
                            similar_count = similar_count+1
                        else:
                            break
                    if (similar_count == len(table_difference[0])):
                        del table_difference[j]
                        break
    # if schema does not match just throw an exception
    else:
        raise MismatchedAttributesException('Schema of tables do not match')
    return table_difference


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

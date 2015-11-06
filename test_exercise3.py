#!/usr/bin/env python

""" Assignment 2, Exercise 3, INF1340, Fall, 2015. DBMS

Test module for exercise3.py

"""

__author__ = "Kei'ichiro Yamamoto, Albert Tai"
__email__ = "keiichiro.yamamoto@mail.utoronto.ca , albert.tai@mail.utoronto.ca"
__copyright__ = "2015 Kei'ichiro Yamamoto, Albert Tai"
__license__ = "MIT License"


from exercise3 import union, intersection, difference, MismatchedAttributesException


###########
# TABLES ##
###########
GRADUATES = [["Number", "Surname", "Age"],
             [7274, "Robinson", 37],
             [7432, "O'Malley", 39],
             [9824, "Darkes", 38]]

MANAGERS = [["Number", "Surname", "Age"],
            [9297, "O'Malley", 56],
            [7432, "O'Malley", 39],
            [9824, "Darkes", 38]]
MANAGERS_WITHOUT_AGE = [["Number", "Surname"],
            [9297, "O'Malley"],
            [7432, "O'Malley"],
            [9824, "Darkes"]]
UOFT_STUDENTS = [["First Name", "Last Name", "Student ID", "Number of Courses"],
                 ["Albert", "Tai", "99902312", 5],
                 ["James", "Falcon", "99502312", 12],
                 ["John", "Dylan", "999032222", 16],
                 ["Sam", "Smith", "99902312", 21]]
RY_STUDENTS = [["First Name", "Last Name", "Student ID", "Number of Courses"],
                 ["Sam", "Smith", "99902312", 21],
                 ["John", "Dylan", "999032222", 16],
                 ["Why", "Me", "999034422", 21],
                 ["Ilike", "Work", "99902312", 25]]

#####################
# HELPER FUNCTIONS ##
#####################
def is_equal(t1, t2):
    return set(map(tuple, t1)) == set(map(tuple, t2))


###################
# TEST FUNCTIONS ##
###################
def test_union():
    """
    Test union operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37],
              [9297, "O'Malley", 56],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, union(GRADUATES, MANAGERS))
def test_union_students():
    """
    Test union operation on students of enrolled in classes at ryerson and toronto
    """
    result = [['First Name', 'Last Name', 'Student ID', 'Number of Courses'],
              ['Albert', 'Tai', '99902312', 5],
              ['James', 'Falcon', '99502312', 12],
              ['John', 'Dylan', '999032222', 16],
              ['Sam', 'Smith', '99902312', 21],
              ['Why', 'Me', '999034422', 21],
              ['Ilike', 'Work', '99902312', 25]]


    assert is_equal(result, union(UOFT_STUDENTS, RY_STUDENTS))
def test_union_invalid_schema():
    """
    Test invalid schema for union operations
    """
    try:
        assert union(MANAGERS, MANAGERS_WITHOUT_AGE)
    except MismatchedAttributesException:
        return True

def test_intersection():
    """
    Test intersection operation.
    """
    result = [["Number", "Surname", "Age"],
              [7432, "O'Malley", 39],
              [9824, "Darkes", 38]]

    assert is_equal(result, intersection(GRADUATES, MANAGERS))
def test_intersection_students():
    """
    Testing intersection operation on students
    """
    result = [['First Name', 'Last Name', 'Student ID', 'Number of Courses'],
              ['John', 'Dylan', '999032222', 16],
              ['Sam', 'Smith', '99902312', 21]]

    assert is_equal(result, intersection(UOFT_STUDENTS, RY_STUDENTS))

def test_intersection_invalid_schema():
    """
    Test invalid schema for intersection operations
    """
    try:
        assert intersection(MANAGERS, MANAGERS_WITHOUT_AGE)
    except MismatchedAttributesException:
        return True


def test_difference():
    """
    Test difference operation.
    """

    result = [["Number", "Surname", "Age"],
              [7274, "Robinson", 37]]

    assert is_equal(result, difference(GRADUATES, MANAGERS))
def test_difference_student():
    """
    Testing difference between student tables
    """

    result = [['First Name', 'Last Name', 'Student ID', 'Number of Courses'],
              ['Albert', 'Tai', '99902312', 5],
              ['James', 'Falcon', '99502312', 12]]

    assert is_equal(result, difference(UOFT_STUDENTS, RY_STUDENTS))
def test_difference_invalid_schema():
    """
    Test invalid schema for difference operations
    """
    try:
        assert difference(MANAGERS, MANAGERS_WITHOUT_AGE)
    except MismatchedAttributesException:
        return True


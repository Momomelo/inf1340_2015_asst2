#!/usr/bin/env python

""" Assignment 2, Exercise 2, INF1340, Fall, 2015. DNA Sequencing

Test module for exercise2.py

"""

__author__ = "Kei'ichiro Yamamoto, Albert Tai"
__email__ = "keiichiro.yamamoto@mail.utoronto.ca , albert.tai@mail.utoronto.ca"
__copyright__ = "2015 Kei'ichiro Yamamoto, Albert Tai"
__license__ = "MIT License"


from exercise2 import find, multi_find

def test_find_basic():
    """
    Test find function with substring that exist
    """
    assert find("This is an ex-parrot", "parrot", 0, 20) == 14

def test_find_none():
    """
    Test find function with substring that does not exist
    """
    assert find("This is an ex-parrot", "help", 0, 20) == -1

def test_find_all():
    """
    Test find function with substring contained multiple times
    """
    assert find("helphelphelphelp", "help", 0, 16) == 0
    assert find("     ", "      ", 0, 10) == -1

def test_find_bad_start_end():
    """
    Test find function with substring that is longer than tested
    """
    try:
        assert find("h", "help", 0, 1)
    except AssertionError:
        return True
def test_find_bad_different_characters():
    """
    Test find function with strings that contain weird characters 
    """
    assert find("@#@#!#@#$%^@&*", "^@&*", 0, 14) == 10

def test_multi_find_basic():
    """
    Test multi_find function.
    """
    assert multi_find("Ni! Ni! Ni! Ni!", "Ni", 0, 20) == "0,4,8,12"

def test_too_many_variables():
    """
    Tests for more variables than are accepted.
    """
    try:
        assert find("asdf", "qwerty", 0, 20, 20) == 10
    except TypeError:
        return True

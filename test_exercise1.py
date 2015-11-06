#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

Test module for exercise1.py

"""

__author__ = "Kei'ichiro Yamamoto, Albert Tai"
__email__ = "keiichiro.yamamoto@mail.utoronto.ca , albert.tai@mail.utoronto.ca"
__copyright__ = "2015 Kei'ichiro Yamamoto, Albert Tai"
__license__ = "MIT License"



from exercise1 import pig_latinify

def test_basic():
    """
    Basic test cases from assignment hand out
    """
    assert pig_latinify("dog") == "ogday"
    assert pig_latinify("scratch") == "atchscray"
    assert pig_latinify("is") == "isyay"
    assert pig_latinify("apple") == "appleyay"

def test_capitals():
    """
    This test case checks if capitals are an acceptable input.
    """
    assert pig_latinify("HELLO WORLD") == "ello worldhay"

def test_symbols():
    """
    This test case checks if symbols are an acceptable input.
    """
    assert pig_latinify("$^&$") == "Error. Does not start with vowel or consonant." 

def test_integer():
    """
    This test case checks if integers are an acceptable input.
    """
    assert pig_latinify(1337) == "Error. Does not start with vowel or consonant."

def test_spaces():
    """
    This test case checks if spaces are an acceptable input.
    """
    assert pig_latinify("     ") == "Error. Does not start with vowel or consonant."

def test_advanced():
    """
    These test strings with a combination of capitals, numbers and symbols
    """
    assert pig_latinify("hell0 W0R|D") == "ell0 w0r|dhay"
    assert pig_latinify("#hashtag") == "Error. Does not start with vowel or consonant."
    assert pig_latinify("   HELLO WORLD") == "Error. Does not start with vowel or consonant."
    assert pig_latinify("0987@#$%*&") == "Error. Does not start with vowel or consonant."
    assert pig_latinify("#Y O L O S W A G 360n0ScoPe") == "Error. Does not start with vowel or consonant."

def test_multiple_variables():
    """
    tests if multiple variables are accepted.
    """
    try:
        assert pig_latinify("afds", "1234")
    except TypeError:
        return True



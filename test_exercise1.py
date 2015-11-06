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


def test_advanced():
    """
    This tests odd cases such as capitals, spaces, symbols, numbers and a mix of them.
    """
    assert pig_latinify("HELLO WORLD") == "ello worldhay"
    assert pig_latinify("hell0 W0R|D") == "ell0 w0r|dhay"
    assert pig_latinify("#hashtag") == "Error. Does not start with vowel or consonant."
    assert pig_latinify("   HELLO WORLD") == "Error. Does not start with vowel or consonant."
    assert pig_latinify("0987@#$%*&") == "Error. Does not start with vowel or consonant."
    assert pig_latinify("#Y O L O S W A G 360n0ScoPe") == "Error. Does not start with vowel or consonant."
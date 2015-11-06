#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = "Kei'ichiro Yamamoto, Albert Tai"
__email__ = "keiichiro.yamamoto@mail.utoronto.ca , albert.tai@mail.utoronto.ca"
__copyright__ = "2015 Kei'ichiro Yamamoto, Albert Tai"
__license__ = "MIT License"


def pig_latinify(word):
    """ This function will make the inputted argument into piglatin.

        :param word: a string or an int.
        :return: a new string.
        :raise: TypeError:
            When more than one variabe is inputted.
    """

    vowel = ["a", "e", "i", "o", "u"]
    consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m",
                 "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

    # Converting word to a string so integers are accepted.
    word = str(word)
    # Convert word to lowercase so capitalization is irrelevant.
    word = word.lower()

    if word[0] in vowel:
        return word + "yay"
    elif word[0] in consonant:
        while word[0] in consonant:
            word = word + word[0]
            word = word[1:]
        return word + "ay"
    else:
        return "Error. Does not start with vowel or consonant."

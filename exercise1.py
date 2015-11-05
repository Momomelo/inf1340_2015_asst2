#!/usr/bin/env python

""" Assignment 2, Exercise 1, INF1340, Fall, 2015. Pig Latin

This module converts English words to Pig Latin words

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

vowel = ["a","e","i","o","u"]
consonant = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

#took out "word" from pig_latinify(word) below
def pig_latinify():
	piglatinchecker = raw_input("Input a string to make it piglatin!").lower()

	if piglatinchecker[0] in vowel:
		print piglatinchecker + "yay"
	elif piglatinchecker[0] in consonant:
		while piglatinchecker[0] in consonant:
			piglatinchecker = piglatinchecker + piglatinchecker[0]
			piglatinchecker = piglatinchecker[1:]
		print piglatinchecker + "yay"
	else:
		print ("Error")

pig_latinify()

#Remove pig_latinify() after you are done the codeself.

"""
if piglatin:

    result = ""

    return result
"""
#^ This above was part of the original code


# Kei'ichi's notes below
"""
	What to do:

		if begins with list vowel, append "yay" to the end
		if word begins with list consonent, remove all consonants until the first vowel then append them to the end of the word. Then add "ay" to the end.
"""

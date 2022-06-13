"""
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.


"""

import re


def first_non_repeating_letter(string):
    non_dupes = []
    for chars in string.lower():
        if string.lower().count(chars) < 2 and chars not in non_dupes:
            non_dupes.append(chars)
    if non_dupes == []:
        return ''
    elif re.search(non_dupes[0], string):
        return non_dupes[0]
    else:
        return non_dupes[0].upper()


"""
def first_non_repeating_letter(string):
    letters = [char for char in string]
    for i in letters:
        if sum([char.lower() == i.lower() for char in letters]) < 2:
            return i
    return ''

"""

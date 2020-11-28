"""
Task:
String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
Notes:

https://leetcode.com/problems/rotate-string/
There is O(n) solutions as well, for instance Knuth–Morris–Pratt algorithm
"""


def is_rotation(string1, string2):
    if len(string1) != len(string2):
        return False
    if len(string1) == 0:
        return True
    length1 = len(string1)
    if length1 == len(string2) and length1 > 0:
        string11 = string1 + string1
        return string2 in string11
    return False


assert is_rotation('abcde', 'cdeab') is True


# simple check O(n^2)
def rotate_string(A, B):
    return len(A) == len(B) and B in A + A

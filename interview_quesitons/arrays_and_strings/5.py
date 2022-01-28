"""
Task:
    One Away: There are three types of edits that can be performed on strings: insert a character,
    remove a character, or replace a character. Given two strings, write a function to check if they are
    one edit (or zero edits) away.
"""


def check_edits(str1, str2):
    if str1 == str2:
        return True
    # insert character or remove character
    if len(str1) != len(str2):
        # check for remove action
        edited = False
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                if edited:
                    return False

                edited = True

                if len(str1) > len(str2):
                    str1 = str1[:i] + str1[i + 1:]
                else:
                    str2 = str2[:i] + str2[i + 1:]
        return True

    if len(str1) == len(str2):
        edited = False
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if edited:
                    return False
                edited = True
        return True

def one_way(s, p):
    if s == p:
        return True

    len_s = len(s)
    len_p = len(p)

    # one charter added/removed
    if len_s != len_p:
        changed = False
        i = 0
        j = 0
        while i < len_p:
            if p[i] != s[j]:
                if changed:
                    return False
                changed = True
                j += 1
                continue
            i += 1
            j += 1
        return True
    # one character changed
    elif len_s == len_p:
        changed = False
        for i in range(len_s):
            if s[i] != p[i]:
                if changed:
                    return False
                changed = True
        return True



assert check_edits('pale', 'pale') is True
assert check_edits('pale', 'ple') is True
assert check_edits('pales', 'pale') is True
assert check_edits('pale', 'bale') is True

assert check_edits('pale', 'bake') is False
assert check_edits('gale', 'bali') is False

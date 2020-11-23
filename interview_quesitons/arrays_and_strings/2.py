"""
Task:
Check Permutation: Given two strings, write a method to decide if one is a permutation of the

Notes:
1) Is permutation comparison is case sensitive (is God a permutation of a dog)?
2) Is white space significant (for this task: yes)?

"""

# pythonic way (or we could sort the strings)
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    if set(str1) == set(str2):
        return True
    return False

# count characters
def check_permutation1(str1, str2):
    letters = {}
    for i in range(len(str1)):
        if str1[i] not in letters:
            letters[str1[i]] = 0

        letters[str1[i]] +=1

    for i in range(len(str2)):
        if str2[i] not in letters:
            return False
        letters[str2[i]] -= 1
        if letters[str2[i]] < 0:
            return False

    return True



assert check_permutation('123', '291') is False

assert check_permutation1('123', '231') is True
assert check_permutation1('123', '291') is False

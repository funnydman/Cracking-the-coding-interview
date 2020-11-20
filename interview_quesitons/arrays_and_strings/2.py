# Check Permutation: Given two strings, write a method to decide if one is a permutation of the


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    if set(str1) == set(str2):
        return True
    return False

print(check_permutation('123', '231'))

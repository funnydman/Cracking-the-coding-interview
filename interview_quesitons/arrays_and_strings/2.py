"""
Task:
Check Permutation: Given two strings, write a method to decide if one is a permutation of the

Questions to ask:
1) Is permutation comparison is case sensitive (is God a permutation of a dog)?
2) Is white space significant (for this task: yes)

"""


def check_permut1(string1, string2):
    if len(string1) != len(string2):
        return False

    return sorted(string1) == sorted(string2)


def check_permut2(string1, string2):
    res = 0
    for n in list(map(ord, string1))+list(map(ord, string2)):
        res ^=n
    return res == 0

def check_permut3(string1, string2):
    adict = {}
    for i, c  in enumerate(string1):
        if c not in adict:
            adict[c] = 0
        adict[c]+=1

    for i, c in enumerate(string2):
        if c not in adict:
            return False
        adict[c]+=-1

        if adict[c] < 0:
            return False
    return True

print(check_permut3("abcd" , "badc"))

print(check_permut3("abcm" , "badc"))


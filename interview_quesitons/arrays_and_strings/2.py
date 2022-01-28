"""
Task:
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

Questions to ask:
1) Is permutation comparison is case sensitive (is God a permutation of a dog)? (for this case: yes)
2) Is white space significant (for this task: yes)
3) Check the character size (ASCII assumed)

"""


# Time complexity: O(n * n log n), Space complexity: O(1), sorting in place
def check_permut1(s1, s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)

# O(n^2), O(n) for map, O(n) for concatetion
def check_permut2(s1, s2):
    res = 0
    for n in list(map(ord, s1)) + list(map(ord, s2)):
        res ^= n
    return res == 0

# Time complexity: O(n), Space complexity O(max(len(s1), len(s2))
def check_permut3(s1, s2):
    if len(s1) != len(s2):
        return False
    table = {}
    for i in range(len(s1)):
        if not s1[i] in table:
            table[s1[i]] = 0
        table[s1[i]] += 1

    for i in range(len(s2)):
        if not s2[i] in table:
            return False
        table[s2[i]] -= 1
        if table[s2[i]] < 0:
            return False
    return True


assert check_permut3("abcd", "badc") is True

assert check_permut3("abcm", "badc") is False


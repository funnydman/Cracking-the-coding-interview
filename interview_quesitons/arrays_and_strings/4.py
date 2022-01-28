"""
Task:
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-
drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
s a real arrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
"""

def is_perm_of_palindrome(string):
    string = string.strip().lower().replace(" ", "")
    l = len(string)
    return len(set(string))==l//2 if len(string) % 2 == 0  else len(set(string))==(l//2 +1)

def is_perm_of_palindrome1(string):
    string = string.strip().lower().replace(" ", "")
    count_odd = 0
    adict = {}

    for c in string:
        if c not in adict:
            adict[c] = 0
        adict[c] += 1

        if adict[c] % 2 == 1:
            count_odd +=1
        else:
            count_odd -=1
    return count_odd <= 1


def toggle_bit(num, pos):
    if num & (1 << pos) != 0:
        return num ^ (1 << pos)
    return num | (1 << pos)


def is_perm_of_palindrome(string):
    string = string.strip().lower().replace(" ", "")
    bit_vector = 0
    for c in string:
        pos = ord(c) - ord("a")
        bit_vector = toggle_bit(bit_vector, pos)
    return bit_vector == 0 or (bit_vector & (bit_vector - 1)) == 0


assert is_perm_of_palindrome("Tact Coa") is True
assert is_perm_of_palindrome("abcba") is True
assert is_perm_of_palindrome("hello") is False



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


assert is_perm_of_palindrome("Tact Coa") is True

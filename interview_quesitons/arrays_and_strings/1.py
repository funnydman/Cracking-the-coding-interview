"""
Task:
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Notes:
1) Check the length of the string, if we assume that all chars are ASCII char then you can't form a string
of 280 unique chars out of a 128-character alphabet (it's okay to assume 256 characters//extended ASCII).


https://leetcode.com/problems/contains-duplicate/
"""

# with sorting O(n*log(n))
def is_unique0(string):
    if len(string) > 128:
        return False
    sorted_str = ''.join(sorted(string))
    for i in range(len(sorted_str) - 1):
        if sorted_str[i] == sorted_str[i + 1]:
            return False
    return True


# handle hashmap for storing chars O(n), space O(1)
def is_unique1(string):
    if len(string) > 128:
        return False

    table = set()
    for i in nums:
        if i in table:
            return False
        table.add(i)
    return True


# We can reduce our space usage by a factor of eight by using a bit vector.
# We will assume, in the below code,
def is_unique2(string):
    checker = 0
    for i in range(len(string)):
        val = ord(string[i]) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val);
    return True

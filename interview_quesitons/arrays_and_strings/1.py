"""
Task:
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Notes:
1) Check the length of the string, if we assume that all chars are ASCII char then you can't form a string
of 280 unique chars out of a 128-character alphabet (it's okay to assume 256 characters//extended ASCII).
2)
"""



# with sorting O(n*log(n))
def is_unique0(string):
    if len(string) > 128:
        return False
    sorted_str = ''.join(sorted(string))
    for i in range(len(sorted_str)-1):
        if sorted_str[i] == sorted_str[i+1]:
            return False
    return True

# handle hashmap for storing chars O(n), space O(1)
def is_unique1(string):
    if len(string) > 128:
        return False

    char_set = set()
    for i in range(len(string)):
        if string[i] in char_set:
            return False
        char_set.add(string[i])
    return True

# We can reduce our space usage by a factor of eight by using a bit vector.
# We will assume, in the below code,
def is_unique2(string):
    checker = 0
    for i in range(len(string)):
        val = ord(string[i]) - ord('a');
        print(checker & (1 << val))
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1<<val);
    return True

is_unique = lambda string: len(set(string)) == len(string)


assert is_unique0('abcdg') == True
assert is_unique0('abcdbg') == False


assert is_unique1('aabcd') == False
assert is_unique1('abc') == True

assert is_unique('aabcd') == False
assert is_unique('abcd') == True


assert is_unique2('aabcd') == False
assert is_unique2('abcd') == True

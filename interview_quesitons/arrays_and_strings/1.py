# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

string  = 'abcdg'

def is_unique(string):
    sorted_str = ''.join(sorted(string))
    for i in range(len(sorted_str)-1):
        if sorted_str[i] == sorted_str[i+1]:
            return False
    return True

print(is_unique(string))

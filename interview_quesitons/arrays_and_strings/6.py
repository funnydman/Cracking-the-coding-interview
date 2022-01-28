"""
Task:
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).


"""


# The runtime is O(p + k^2), p is size of the original string, k is the num of character sequences
def string_compression(string):
    if not string:
        return string

    compressed_str = ''
    count = 0
    for i in range(len(string)):
        count += 1

        if i + 1 >= len(string) or string[i] != string[i + 1]:
            compressed_str += string[i] + str(count)
            count = 0

    if len(compressed_str) > len(string):
        return string

    return compressed_str

# Using two pointers:
def string_compression(string):
    if not string:
        return string

    compressed_str = ''
    count = 0

    slow = fast = 0

    while fast < len(string) and slow <= fast:
        if string[slow] == string[fast]:
            count += 1
            fast += 1
        else:
            compressed_str += string[slow] + str(count)
            slow = fast
            count = 0

    if count:
        compressed_str += string[slow] + str(count)

    if len(compressed_str) > len(string):
        return string

    return compressed_str


assert string_compression('') == ''
assert string_compression('a') == 'a'
assert string_compression('aaabc') == 'aaabc'
assert string_compression('aaaaaaaaabc') == 'a9b1c1'
assert string_compression('aabbbg') == 'a2b3g1'
assert string_compression('abc') == 'abc'

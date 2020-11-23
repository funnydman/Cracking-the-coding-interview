"""
Task:
URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)

"""

def strip(string):
    i = 0
    l  = len(string)
    while i < l:
        if string[0] == ' ':
            string = string[1:]

        if string[-1] == ' ':
            string = string[:-1]
        i+=1
    return string

def encode_space(string, symbol='%20'):
    alist = list(string)
    for i in range(len(alist)):
        if alist[i] == ' ':
            alist[i] = symbol
    return ''.join(alist)

def encode_space1(string, symbol='%20'):
    new_str = ''
    for i in string:
        if i == ' ':
            new_str += symbol
        else:
            new_str += i
    return new_str

assert encode_space(strip('              a  b c   ')) == 'a%20%20b%20c'

assert encode_space1(strip('a bc')) == 'a%20bc'


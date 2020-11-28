"""
Task:
String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").

Notes:
1) We can reduce the space to 0 (1) by using the first row as a replacement for the row array and the first
column as a replacement for the column array.
"""


def set_zeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])

    coordinates = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                coordinates[i][j] = 1

    for i in range(m):
        for j in range(n):
            if coordinates[i][j] == 1:
                for k in range(n):
                    matrix[i][k] = 0
                # zeroing the column
                for c in range(m):
                    matrix[c][j] = 0

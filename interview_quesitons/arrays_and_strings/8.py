"""
Task:
String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").

Notes:
1) We can reduce the space to 0 (1) by using the first row as a replacement for the row array and the first
column as a replacement for the column array.

https://leetcode.com/problems/set-matrix-zeroes/
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
                
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            if matrix[i][0] == 0: col0 = 0
            for j in range(1, cols):
                if matrix[i][j]== 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, 0, -1):
                if (matrix[i][0] == 0 or matrix[0][j] == 0):
                    matrix[i][j] = 0
                if col0 == 0:
                    matrix[i][0] = 0




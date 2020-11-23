"""
Task:
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
Notes:

1) Implement withot allocating another 2d matrix
leetcode: https://leetcode.com/problems/rotate-image/solution/
"""

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

res = [
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

n = len(matrix)
m = len(matrix[0])

def rotate(matrix):

    for i in range(n):
        for j in range(i, m):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    for i in range(n):
        matrix[i].reverse()
    return matrix

assert rotate(matrix) == res

# rotate four rectangles

def rotate1(matrix):
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = [0] * 4
            row, col = i, j
            # store 4 elements in tmp
            for k in range(4):
                tmp[k] = matrix[row][col]
                row, col = col, n - 1 - row
            # rotate 4 elements
            for k in range(4):
                matrix[row][col] = tmp[(k - 1) % 4]
                row, col = col, n - 1 - row
    return matrix

# Rotate four rectangles in one single loop
def rotate3(matrix):
    for i in range(n // 2 + n % 2):
        for j in range(n // 2):
            tmp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
            matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp
    return matrix

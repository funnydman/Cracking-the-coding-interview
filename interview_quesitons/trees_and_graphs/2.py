"""
Task:
Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.

Follow up: how to convert a linked list?
"""
from general import TreeNode


def create_minimal_bst(alist, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    n = TreeNode(alist[mid])
    n.left = create_minimal_bst(alist, start, mid - 1)
    n.right = create_minimal_bst(alist, mid + 1, end)
    return n


alist = [-10, -3, 0, 5, 9]
tree = create_minimal_bst(alist, 0, len(alist) - 1)

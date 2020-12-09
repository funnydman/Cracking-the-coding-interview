"""
Task:
Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a binary search tree with minimal height.
"""

def create_minimal_bst(alist, start, end):
    if end < start:
        return None
    mid = (start + end) // 2
    n = Tree(alist[mid])
    n.left = create_minimal_bst(alist, start, mid - 1)
    n.right = create_minimal_bst(alist, mid + 1, end)
    return n


tree = create_minimal_bst(alist, 0, len(alist) - 1)

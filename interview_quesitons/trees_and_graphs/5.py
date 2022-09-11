"""
Task:
Validate 8ST: Implement a function to check if a binary tree is a binary search tree.
Notes:
    1 approach - use in order traversal and check elements (they must in inc order).
    fix: change from root.val > _max to root.val >= _max
    https://leetcode.com/problems/validate-binary-search-tree/
"""

from general import TreeNode

root = TreeNode(7)
root.left = TreeNode(5)
root.right = TreeNode(10)

root.left.left = TreeNode(3)
root.left.right = TreeNode(6)

root.right.right = TreeNode(11)
root.right.left = TreeNode(8)


def check_bst(root, _min=float('-inf'), _max=float('inf')):
    if root is None:
        return True

    if root.val <= _min or root.val > _max:
        return False

    if not check_bst(root.left, _min, root.val):
        return False
    if not check_bst(root.right, root.val, _max):
        return False

    return True


assert check_bst(root) is True

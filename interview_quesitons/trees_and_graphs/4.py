"""
Task:
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""
from general import TreeNode


def _is_balanced(self, root):
    if root is None:
        return -1

    left_height = self._isBalanced(root.left)
    if left_height == float('-inf'):
        return float('-inf')
    right_height = self._isBalanced(root.right)
    if right_height == float('-inf'):
        return float('-inf')

    diff = abs(left_height - right_height)

    if diff > 1:
        return float('-inf')
    else:
        return max(left_height, right_height) + 1

def is_balanced(self, root: TreeNode) -> bool:
    return self._isBalanced(root) != float('-inf')

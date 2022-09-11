"""
Task:
First Common Ancestor: Design an algorithm and wri te code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
Notes:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/
"""
from general import TreeNode

root = TreeNode(7)
root.left = TreeNode(5)
root.right = TreeNode(10)

root.left.left = TreeNode(3)
root.left.right = TreeNode(6)

root.right.right = TreeNode(11)
root.right.left = TreeNode(8)


def lowest_common_ancestor(root, p, q):
    if root == p or root == q:
        return root

    left = right = None

    if root.left:
        left = lowest_common_ancestor(root.left, p, q)
    if root.right:
        right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right


def lowest_common_ancestor2(root, p, q):
    ans = None

    def helper(curr):
        nonlocal ans
        if not curr:
            return False
        left = helper(curr.left)

        right = helper(curr.right)

        mid = curr == p or curr == q

        if mid + left + right >= 2:
            ans = curr

        return mid or left or right

    helper(root)
    return ans


print(lowest_common_ancestor(root, root.right.left, root.left.left))

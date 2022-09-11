class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


"""
              1
        2          3
    4       5
       7       6
"""

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.left.right = TreeNode(7)

root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)

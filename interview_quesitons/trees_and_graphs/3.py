"""
Task:
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
Todo: implement with bfs as well
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.left.right = Node(7)

root.left.right = Node(5)
root.left.right.right = Node(6)

def create_level_linked_list(root, alist, level):
    if root is None:
        return
    if len(alist) == level:
        l = []
        alist.append(l)
    else:
        l = alist[level]

    l.append(root.val)
    create_level_linked_list(root.left, alist, level + 1)
    create_level_linked_list(root.right, alist, level + 1)

    return alist


print(create_level_linked_list(root, [], 0))
# [[1], [2, 3], [4, 5], [7, 6]]

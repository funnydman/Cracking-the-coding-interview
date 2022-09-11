"""
Task:
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
Todo: implement with bfs as well
"""

from general import root


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


assert create_level_linked_list(root, [], 0) == [[1], [2, 3], [4, 5], [7, 6]]

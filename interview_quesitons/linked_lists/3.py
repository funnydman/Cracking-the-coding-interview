"""
Task:
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

https://leetcode.com/problems/delete-node-in-a-linked-list/
"""
from general import *

head = build_from_list([1, 2, 3, 4, 5])


# Simply copy data from the next and to the current node
# and make pointing current node to the next next node.
# Cannot be solved if the node to be deleted is the last node in the linked list
def delete_node(node):
    if not node or not node.next:
        return False

    node.data = node.next.data
    node.next = node.next.next

    return True


delete_node(node)
print_list(head)

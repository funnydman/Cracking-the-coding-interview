"""
Task:
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.

"""
from general import *

head = build_from_list([1, 2, 3, 4, 5])


def get_by_index(head, index):
    current = head
    i = 0
    while current != None:
        if i == index:
            return current
        current = current.next
        i += 1
    raise IndexError


node = get_by_index(head, 2)


# Simply copy data from the next and to the current node
# and make pointing current node to the next next node.
# Cannot be solved if the node to be deleted is the last node in the linked list
def delete_node(node):
    if node is None or node.next is None:
        return False

    node.data = node.next.data
    node.next = node.next.next

    return True

def delete_middle_node(node):
    temp = node
    temp.val = temp.next.val

    temp.next = temp.next.next


delete_node(node)
print_list(head)

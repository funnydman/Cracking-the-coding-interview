"""
Task:
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
"""

from general import *

head = build_from_list([1, 4, 3, 2, 5, 2])


def partition(head, x):
    curr = head

    before = before_head = Node(None)
    after = after_head = Node(None)

    while curr:
        if curr.data < x:
            before.next = Node(curr.data)
            before = before.next
        else:
            after.next = Node(curr.data)
            after = after.next

        curr = curr.next

    after.next = None
    before.next = after_head.next

    return before_head.next


head = partition(head, 3)

print_list(head)

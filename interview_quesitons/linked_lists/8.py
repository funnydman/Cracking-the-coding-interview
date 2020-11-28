"""
Task:
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A - > B - > C - > D - > E - > C [the same C as earlier)
Output: C
"""

from general import *

head = build_from_list([3, -4])

head.next.next = head.next


def is_loop(head):
    d  = []
    cur1 = head
    while cur1 != None:
        if cur1 in d:
            return True
        else:
            d.append(cur1)
        cur1 = cur1.next
    return False


def is_loop1(head):
    slow = head
    fast = head.next

    while fast != slow:
        if fast == None or fast.next == None:
            return False

        slow = slow.next
        fast = fast.next.next

    return True

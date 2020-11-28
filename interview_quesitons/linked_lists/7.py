"""
Task:
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the headA linked list is the exact same node (by reference) as the jth node of the headB
linked list, then they are intersecting.
"""

from general import *

headA = build_from_list([4, 1])

headB = build_from_list([5, 6, 1])

headA.next = headB.next = Node(8)
headA.next.next = headB.next.next = Node(4)
headA.next.next.next = headB.next.next.next = Node(5)


def interseciton(headA, headB):
    cur1, cur2 = headA, headB

    len1 = len2 = 0

    while cur1.next:
        len1 += 1
        cur1 = cur1.next

    while cur2.next:
        len2 += 1
        cur2 = cur2.next

    if cur1 is not cur2:
        return

    cur1, cur2 = headA, headB

    diff = abs(len1 - len2)
    node = cur1 if max(len1, len2) == len1 else cur2

    for _ in range(diff):
        node = node.next
    while cur1 and cur2:
        if cur1 is cur2:
            return cur1.data
        cur1 = cur1.next
        cur2 = cur2.next
    return


print(interseciton(headA, headB))

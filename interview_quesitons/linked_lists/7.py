"""
Task:
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
intersecting node. Note that the intersection is defined based on reference, not value. That is, if the
kth node of the headA linked list is the exact same node (by reference) as the jth node of the headB
linked list, then they are intersecting.
"""

from general import *

headA = build_from_list([4, 1])

headB = build_from_list([5])

headA.next.next = headB.next = Node(8)
headA.next.next.next = headB.next.next = Node(5)


def intersection(headA, headB):
    cur1, cur2 = headA, headB

    len1 = len2 = 0

    while cur1:
        len1 += 1
        cur1 = cur1.next

    while cur2:
        len2 += 1
        cur2 = cur2.next

    if cur1 is not cur2:
        return

    cur1, cur2 = headA, headB

    diff = abs(len1 - len2)
    m = max(len1, len2)

    for _ in range(diff):
        if m == len1:
            cur1 = cur1.next
        else:
            cur2 = cur2.next

    while cur1 and cur2:
        if cur1 is cur2:
            return cur1.data
        cur1 = cur1.next
        cur2 = cur2.next
    return


def intersection1(head_A, head_B):
    if head_A == None or head_B == None:
        return None

    a_pointer = headA
    b_pointer = headB

    while a_pointer != b_pointer:
        a_pointer = headB if a_pointer == None else a_pointer.next
        b_pointer = headA if b_pointer == None else b_pointer.next

    return a_pointer


print(intersection(headA, headB))

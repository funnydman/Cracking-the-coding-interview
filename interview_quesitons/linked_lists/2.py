"""
Task:
    Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
"""

from general import *

head = build_from_list([1, 2, 3, 4, 5])

# Solution 1: If linked list size is known
# if linked list size is known -> solution is trivial, then the kth to last is the (length - k)th element.

# Solution 2: Recursive
# Don't return the element
# def k_to_last(head, k):
#     if head is None:
#         return 0
#     index = k_to_last(head.next, k, i)
#     i+=1
#     if index == k:
#         print(k, 'th to the last node is', head.data)
#     return index

# k_to_last(head, 2)

# Solution 3: Iterative
def k_to_last(head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

head = k_to_last(head, 2)
print_list(head)

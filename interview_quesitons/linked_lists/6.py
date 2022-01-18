"""
Implement a function to check if a linked list is a palindrome.
Todo: implement recursively

https://leetcode.com/problems/palindrome-linked-list/
"""

from general import *

head = build_from_list([1, 2, 7, 2, 1])


def reverse_list(head):
    curr = head
    last = None
    while curr != None:
        n = Node(curr.data)
        n.next = last

        last = n

        curr = curr.next
    return last


# reverse and compare
def is_palindrome(head):
    reversed_list = reverse_list(head)
    print_list(reversed_list)
    while head and reversed_list:
        print(head.data, reversed_list.data)
        if head.data != reversed_list.data:
            return False

        head = head.next
        reversed_list = reversed_list.next

    return not head and not reversed_list


# Iterative Approach (with stack)
def is_palindrome1(head):
    fast = slow = head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # has odd number of elements, so skip the middle element
    if fast != None:
        slow = slow.next

    while slow != None:
        top = stack.pop()
        if top != slow.data:
            return False

        slow = slow.next

    return True


print(is_palindrome1(head))

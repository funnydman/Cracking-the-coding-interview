"""
Task:
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
Todo:
    Write solution for the case when numbers have different length.
"""

from general import *

list1 = build_from_list([7, 1, 6])
list2 = build_from_list([5, 9, 2])


# assume that linked lists have the same length.
def sum_lists(list1, list2):
    curr = curr_head = Node(None)
    curry = 0

    while list1 != None:
        res = list1.data + list2.data + curry

        a = res % 10
        curry = res >= 10

        curr.next = Node(a)
        curr = curr.next

        list1 = list1.next
        list2 = list2.next
    return curr_head.next



def sum_lists_forward(first, second):
    curr = curr_head = Node(None)
    res = 0

    length = 0
    temp = first
    while temp:
        length += 1
        temp = temp.next

    i = length - 1
    while first != None:
        res += (first.val + second.val) * 10**i
        i -=1


        first = first.next
        second = second.next


    i = length - 1
    while res != 0:
        a = res // 10**i

        res = res % 10**i


        curr.next = Node(a)
        curr = curr.next
        i -=1

    return curr_head.next


head = sum_lists(list1, list2)

# 9 -> 1 ->2
print_list(head)

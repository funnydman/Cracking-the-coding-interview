"""
Task:
Remove Dups: Write code to remove duplicates from an unsorted li nked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
Notes:

"""

from general import *

head = build_from_list([1, 5, 3, 1, 2])


# takes O(n) time, O(n) space
def delete_duplicates(head: Node):
    seen = set()
    prev = Node(-1)

    temp = head

    while temp:
        if temp.value in seen:
            prev.next = temp.next
        else:
            seen.add(temp.value)
            prev = temp

        temp = temp.next
    return head


# follow up: no buffer allowed O(n^2) time, O(1) space
# using nested while
def delete_duplicates(head: Node):
    current = head

    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return head


delete_dups(head)
print_list(head)

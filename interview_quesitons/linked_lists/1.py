"""
Task:
Remove Dups: Write code to remove duplicates from an unsorted li nked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
Notes:

"""

from general import *

head = build_from_list([1, 5, 3, 1, 2])

# takes O(n) time
def delete_duplicates(head: Node):
    alist = []
    previous = Node(None)

    while head != None:
        if head.data in alist:
            previous.next = head.next
        else:
            alist.append(head.data)
            previous = head

        head = head.next

# follow up: no buffer allowed O(n^2) time, O(1) space
# using nested while

def delete_dups(head):
    current = head
    while current != None:
        runner = current
        while runner.next != None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

delete_dups(head)
print_list(head)

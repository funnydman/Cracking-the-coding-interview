class Node:
    def __init__(self, data: int):
        self.next = None
        self.data = data

    def __str__(self):
        return f'<data={self.data}>'


def add(head: Node, value: int) -> None:
    end = Node(value)

    current = head
    while current.next != None:
        current = current.next

    current.next = end


def print_list(head: Node):
    current = head
    while current != None:
        print(current)
        current = current.next


def build_from_list(alist: list) -> 'Node':
    if not alist:
        return None

    head = Node(alist[0])
    current = head
    for i in alist[1:]:
        current.next = Node(i)
        current = current.next
    return head


# delete node from a single linked list
def delete_node(head: Node, value: int):
    current = head

    if head is None:
        return head

    if head.data == value:
        return head.next

    while current.next != None:
        if current.next.data == value:
            current.next = current.next.next
            return head
        current = current.next

    raise Exception('Element not found')

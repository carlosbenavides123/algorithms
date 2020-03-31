# reverse a linked list given a boundary inclusive
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


head = Node(11, Node(3, Node(5, Node(7, Node(2)))))


def reverse(head, start, end):
    dummy_head = sublist_head = Node(0, head)

    for _ in range(1, start):
        sublist_head = sublist_head.next
    sublist_iter = sublist_head.next
    for _ in range(end - start):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
    return dummy.next


print(reverse(head, 2, 4))

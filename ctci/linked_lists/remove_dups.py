# remove duplicates from an unsorted linkedlist


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


head = Node(2, Node(3, Node(4, Node(5, Node(2, Node(4, Node(8)))))))


# 2 -> 3 -> 4 -> 5 -> 2 -> 4 -> 8

# expected 2 -> 3 -> 4 -> 5 -> 8

def print_nodes(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


def remove_dups(head):
    seen = set()
    dummy = Node(0, head)
    curr = head.next
    prev = head
    seen.add(prev.val)
    while curr != None:
        if curr.val not in seen:
            seen.add(curr.val)
            prev = curr
        else:
            prev.next = curr.next
        curr = curr.next
#    print_nodes(head)
    return head


remove_dups(head)


# dumb ctci question?

# 2 -> 3 -> 3 -> 4 -> 4 -> 4 -> 23 -> 1 -> 1 -> 2 -> 2
# expected 2 -> 3 -> 4 -> 23 -> 1 -> 2

head = Node(2, Node(3, Node(
    3, Node(4, Node(4, Node(4, Node(23, Node(1, Node(1, Node(2, Node(2)))))))))))

# print_nodes(head)


def remove_dups(head):
    curr = head
    while curr:
        curr_next = curr.next
        while curr_next and curr.val == curr_next.val:
            curr.next = curr_next.next
            curr_next = curr_next.next
        curr = curr.next
    print_nodes(head)


remove_dups(head)

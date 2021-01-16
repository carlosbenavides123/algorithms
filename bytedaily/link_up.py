# This question is asked by Facebook. Given a singly linked list, re-order and group its nodes in such a way
# that the nodes in odd positions come first and the nodes in even positions come last.

# Ex: Given the reference to the following linked list...

# 4->7->5->6->3->2->1->NULL, return 4->5->3->1->7->6->2->NULL
# Ex: Given the reference to the following linked list...

# 1->2->3->4->5->NULL, return 1->3->5->2->4->NULL

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

linked_list = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# 1->2->3->4->5->NULL

# 1 -> 3 -> 2 -> 4 -> 5 -> Null

# 1 -> 3 -> 2 -> 5 -> 4 -> Null

# first position never stays, keep a pointer there
#
# we can assume at least 3 items correct?

# 1 -> 2 -> 3 -> Null
# 1 -> 3 -> 2 -> Null

# each iteration move three positions, save it as temp

# swap 3rd pos with 2nd pos
# swap 2nd pos with 3rd pos
# 1 links to 3, 3 links to 2, 2 links to the temp
def link_up(linked_list):
    head = linked_list
    odd_links = head
    even_links = even_start = head.next

    while even_links and even_links.next:
        odd_links.next = even_links.next
        odd_links = odd_links.next
        even_links.next = even_links.next.next
        even_links = even_links.next
    odd_links.next = even_start
    print_list(head)
    return head

def print_list(ll):
    while ll:
        print(ll.val)
        ll = ll.next

print(link_up(linked_list))

# 4->7->5->6->3->2->1->NUL
# return 4->5->3->1->7->6->2->NULL
ll = Node(4, Node(7, Node(5, Node(6, Node(3, Node(2, Node(1)))))))
print(link_up(ll))

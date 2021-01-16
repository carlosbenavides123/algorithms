# Given two linked lists that represent two numbers, return the sum of the numbers also represented as a list.

# Ex: Given the two linked lists…

# a = 1->2, b = 1->3, return a list that looks as follows: 2->5
# Ex: Given the two linked lists…

# a = 1->9, b = 1, return a list that looks as follows: 2->0

class Node():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

num_list_1 = Node(1, Node(2))
num_list_2 = Node(1)

def reverse_num_list(num_list):
    prev = None
    temp = None
    while num_list:
        temp = num_list.next
        num_list.next = prev
        prev = num_list
        num_list = temp
    return prev

def list_sum(num_list_1, num_list_2):
    dummy = cur = Node(-1)
    dummy.next = cur
    cur_sum = 0

    reversed_num_list_1 = reverse_num_list(num_list_1)
    reversed_num_list_2 = reverse_num_list(num_list_2)

    while reversed_num_list_1 or reversed_num_list_2:
        num_1 = num_2 = 0
        if reversed_num_list_1:
            num_1 = reversed_num_list_1.val
            reversed_num_list_1 = reversed_num_list_1.next
        if reversed_num_list_2:
            num_2 = reversed_num_list_2.val
            reversed_num_list_2 = reversed_num_list_2.next
        cur_sum += (num_1 + num_2)
        cur.next = Node(cur_sum%10)
        cur = cur.next
        cur_sum //= 10
    dummy = reverse_num_list(dummy.next)
    print_list(dummy)
    return dummy

def print_list(num_list):
    s = ""
    while num_list:
        s += str(num_list.val)
        num_list = num_list.next
    print(s)

print(list_sum(num_list_1, num_list_2))


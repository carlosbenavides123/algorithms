# given two non empty linked lists, digits are stored in reverse order and each of their nodes contain
# a single digit
# add them

class Node:
    def __init__(self, val, Next=None):
        self.val = val
        self.Next = Next

# num1 = Node(3, Node(2))
# num2 = Node(5, Node(4))
num1 = Node(3)
num2 = Node(5, Node(5, Node(5)))

def add_two_nums(num1, num2):
    dummy_node = curr = Node(-1)
    curr_val = 0
    while num1 or num2 or curr_val:
        num1_val = 0
        num2_val = 0
        if num1 != None:
            num1_val = num1.val
            num1 = num1.Next
            
        if num2 != None:
            num2_val = num2.val
            num2 = num2.Next
        curr_val += num1_val + num2_val
        curr.Next = Node(curr_val % 10)
        curr = curr.Next
        print(curr_val%10)
        curr_val //= 10
    return dummy_node.Next
print(add_two_nums(num1, num2))


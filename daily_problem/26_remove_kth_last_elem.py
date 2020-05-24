#This problem was asked by Google.

#Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

#The list is very long, so making more than one pass is prohibitively expensive.

#Do this in constant space and in one pass.

# 1 - 2 - 3 - 4 - 5 - 6
# k = 2
# remove 4

class Node():
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

node = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))

k = 2
def remove_kth_last_elem(node, k):
	fast = res = node
	while k:
		k -= 1
		fast = fast.next
	curr = res
	while fast.next != None:
		curr = curr.next
		fast = fast.next
	curr.next = curr.next.next
	while res != None:
		print(res.val)
		res = res.next
	return res
print(remove_kth_last_elem(node, k))
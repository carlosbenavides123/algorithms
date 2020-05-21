#This problem was asked by Google.

#Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

#For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

#In this example, assume nodes with the same value are the exact same node objects.

#Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node():
	def __init__(self, val, next=None):
		self.val = val
		self.next = next

node_list_1 = Node(3, Node(7, Node(8, Node(10))))
node_list_2 = Node(99, Node(1, Node(8, Node(10))))

def get_node_length(node):
	if not node:
		return 0
	return 1 + get_node_length(node.next)

def sol(node_list_1, node_list_2):
	n, m = get_node_length(node_list_1), get_node_length(node_list_2)
	if n > m:
		for _ in range(n - m):
			node_list_1 = node_list_1.next
	else:
		for _ in range(m - n):
			node_list_2 = node_list_2.next
	while node_list_1.val != node_list_2.val:
		node_list_1 = node_list_1.next
		node_list_2 = node_list_2.next
	return node_list_1.val
		
print(sol(node_list_1, node_list_2))

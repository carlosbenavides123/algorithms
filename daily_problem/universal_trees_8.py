#This problem was asked by Google.

#A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

#Given the root to a binary tree, count the number of unival subtrees.

#For example, the following tree has 5 unival subtrees:

 #  0
 # / \
 #1   0
 #   / \
 #  1   0
 # / \
 #1   1

# travel all the way to leaf
# if we reach a none, return 0, and true
# we have be cautioness about
#  0
# /
#_ 0
# / \ 
#_   _
# we need to make sure the right subtree is unival
# we can just say
#  0
# / \
# x  y
# x == y... without exploring alll of x and y
 
class Node():
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

root = Node(0)

sub1left = Node(1)
sub1right = Node(0, left=Node(1, Node(1), Node(1)), right=Node(0))

root.left = sub1left
root.right = sub1right

def solve(root):
	count, _ = rec(root)
	return count

def rec(root):
	if not root:
		return 0, True
	left_count, is_left_unival = rec(root.left)
	right_count, is_right_unival = rec(root.right)
	total = left_count + right_count
	if is_left_unival and is_right_unival:
		if root.left != None and root.left.val != root.val:
			return total, False
		if root.right != None and root.right.val != root.val:
			return total, False
		return total + 1, True
	return total, False

print(solve(root))

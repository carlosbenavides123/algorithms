# Given the reference to a binary search tree, return the kth smallest value in the tree.

# Ex: Given the following binary search tree and value k…

#     3
#    / \
#   2   4, k = 1, return 2.
# Ex: Given the following binary search tree and value k…

#     7
#    / \
#   3   9
#    \
#     5, k = 3, return 7

class Node():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    res = [k, 0]
    recurse_kth_smallest(root, res)
    return res[1]
    stk = [root]
    while stk or root:
        while root:
            stk.append(root)
            root = root.left
        root = stk.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
    return root.val

def recurse_kth_smallest(root, res):
    if root.left:
        recurse_kth_smallest(root.left, res)

    res[0] -= 1
    if res[0] == 0:
        res[1] = root.val
        return

    if root.right:
        recurse_kth_smallest(root.right, res)


tree = Node(3, Node(2), Node(4))
print(kth_smallest(tree, 2))
tree = Node(7, Node(3, None, Node(5)), Node(9))
print(kth_smallest(tree, 3))

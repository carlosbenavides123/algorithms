# Given root to a binary tree
# implement serialize(root) wich 
# serializes into a string
# deserializes back to a tree
import collections

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#   1
#  2  3
# 4 5 6 7

def solve(root):
    string = serialize(root)
    print(string)
    
    root = deserialize(string)
    q = collections.deque([root])
    while q:
        arr = []
        new_q = collections.deque([])
        for item in q:
            if item:
                arr.append(item.val)
                if item.left:
                    new_q.append(item.left)
                if item.right:
                    new_q.append(item.right)
            else:
                arr.append(None)
            
        print(arr)
        q = new_q
        

def serialize(root):
    if not root:
        return
    q = collections.deque([root])
    serialize = []
    while q:
        node = q.popleft()
        if not node:
            serialize += "#"
            continue
        serialize.append(str(node.val))
        q.append(node.left)
        q.append(node.right)
    return ','.join(serialize)

            
def deserialize(string):
    if not string:
        return
    data = string.split(",")
    index = 0
    root = TreeNode(int(data[index]))
    q = collections.deque([root])
    while q:
        node = q.popleft()
        index += 1
        if data[index] != "#":
            node.left = TreeNode(int(data[index]))
            q.append(node.left)
        else:
            node.left = None

        index += 1
        if data[index] != "#":
            node.right = TreeNode(int(data[index]))
            q.append(node.right)
        else:
            node.right = None
    return root

tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3, left=TreeNode(6), right=TreeNode(7)))

print(solve(tree))

tree = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)))
print(solve(tree))

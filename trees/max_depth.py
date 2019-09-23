# Maximum Depth of Binary Tree
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.
# O(n) time and O(logn) space both


class Solution(object):
    def maxDepth(self, root):
        depth = 0
        level = [root] if root else []
        while level:
            depth += 1
            queue = []
            for el in level:
                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            level = queue

        return depth

# or


class Solution(object):
    def maxDepth(self, root):
        return self.preorder(root, 0)

    def preorder(self, root, count):
        if root == None:
            return count
        res = 0
        res = max(res, self.preorder(root.left, count + 1))
        res = max(res, self.preorder(root.right, count + 1))
        return res

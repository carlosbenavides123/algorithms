# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_list = self.getPath(root, p.val)
        q_list = self.getPath(root, q.val)

        if p_list == [] or q_list == []:
            return None

        res = None
        while p_list and q_list:
            p_node, q_node = p_list.pop(), q_list.pop()
            if p_node == q_node:
                res = p_node
            else:
                break
        return res

    def getPath(self, root, X):
        if root == None:
            return None
        if root.val == X:
            return [root]
        leftPath = self.getPath(root.left, X)
        if leftPath != None:
            leftPath.append(root)
            return leftPath
        rightPath = self.getPath(root.right, X)
        if rightPath != None:
            rightPath.append(root)
            return rightPath
        return None

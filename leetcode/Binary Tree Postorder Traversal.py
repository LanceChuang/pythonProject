# Binary Tree Postorder Traversal
# Given a binary tree, return the postorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],

#    1
#     \
#      2
#     /
#    3
 

# return [3,2,1].

# Note: Recursive solution is trivial, could you do it iteratively?
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        # if root.left is None and root.right is None: return [root.val]
        # Postorder (Left, Right, Root) 
        # pre order first , then reverse it
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]
        
        
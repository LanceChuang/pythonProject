# Binary Tree Preorder Traversal
# Given a binary tree, return the preorder traversal of its nodes' values.

# For example:
# Given binary tree [1,null,2,3],
#    1
#     \
#      2
#     /
#    3
# return [1,2,3].
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        res = []
        # preorder is root->left->right so use DFS and stack
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val) # root
                stack.append(node.right)
                stack.append(node.left) # left放後面因為會先被pop
                
        return res


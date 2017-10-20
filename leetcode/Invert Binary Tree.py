# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Thinking:
# (1)  Call Mirror for left-subtree    i.e., Mirror(left-subtree)
# (2)  Call Mirror for right-subtree  i.e., Mirror(right-subtree)
# (3)  Swap left and right subtrees.
#           temp = left-subtree
#           left-subtree = right-subtree
#           right-subtree = temp   
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: # if no tree, return root itself
            return root
        self.mirror(root)

        return root

    def mirror(self,root):
        if not root:
            return root
        # swap left tree and right tree
        left_node = self.mirror(root.left)
        right_node = self.mirror(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        
        return root
        
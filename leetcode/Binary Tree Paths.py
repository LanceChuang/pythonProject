# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:
#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        output = []
        
        def rootToleaf(root,String):
            # left, right 都是null，代表已經到了leaf，一條路徑完成
            if root.left == None and root.right == None:
                output.append(String+str(root.val)) # 走完一條路徑放到list
            # else:
            if root.left != None:
                rootToleaf(root.left,String+str(root.val)+"->")
            if root.right != None:
                rootToleaf(root.right,String+str(root.val)+"->")
            

        rootToleaf(root,"")
        return output
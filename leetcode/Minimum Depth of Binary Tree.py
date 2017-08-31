# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along
#  the shortest path from the root node down to the nearest leaf node.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        compare = []
        def findPath(root,count):
            if root.left == None and root.right == None:
                count += 1
                compare.append(count)
                return 
            if root.left != None and root.right == None:
                return findPath(root.left,count+1)
            if root.right != None and root.left == None:
                return findPath(root.right,count+1)
            # 假如左右都還沒到底
            return findPath(root.left,count+1) or findPath(root.right,count+1) 
        findPath(root,0)
        answer = min(compare)
        # print(compare)
        return  answer

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b
a.right = c

Sol = Solution()
ans = Sol.minDepth(a)
print(ans)

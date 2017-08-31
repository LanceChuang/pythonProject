# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
#  such that adding up all the values along the path equals the given sum.

# For example:
# Given the below binary tree and sum = 22
      #         5
      #        / \
      #       4   8
      #      /   / \
      #     11  13  4
      #    /  \      \
      #   7    2      1

# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, Sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        # 一開始root[5]，總和s = 0，先計算左節點再來右節點
        temp = []
        
        def sumR2L(root,s):
            # 到底的時候，判斷總和是否與sum相同 
            if root.left == None and root.right == None:
                s += root.val
                temp.append(s)
                return s == Sum
            
            # 左邊還沒到底，右邊已經到底，繼續計算左樹的總和
            if root.left != None and root.right == None:
                return sumR2L(root.left, s+root.val)
            
            # 右邊還沒到底，左邊已經到底，繼續計算右邊的總和
            if root.left == None and root.right != None:
                return sumR2L(root.right, s+root.val)
            
            # 兩邊的樹都還沒到底，繼續分別計算總和，因為只要有一條路徑成立就是true，因此使用 or來判斷
            return sumR2L(root.left, s+root.val) or sumR2L(root.right, s+root.val)
        sumR2L(root,0)
        # print(temp)
        return sumR2L(root,0)


    def hasPathSum2(self, root, sum): # 使用減去的方式
        if not root: 
            return False

        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(8)
d = TreeNode(11)
e = TreeNode(13)
f = TreeNode(4)
a.left = b
a.right = c
b.left = d
c.left = e 
c.right = f 

answer = Solution()
ans = answer.hasPathSum2(a,10)
print(ans)

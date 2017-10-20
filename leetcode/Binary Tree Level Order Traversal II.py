# Given a binary tree, return the bottom-up level order traversal of its 
# nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

  #   3
  #  / \
  # 9  20
  #   /  \
  #  15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
import collections
# Thinking1: 用一般BFS方式，最後反轉list順序  

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        ans = []
        level = [root]
        
        while level :
            ans.append([n.val for n in level])
            # next = []
            # for node in level:
                # next.extend([node.left,node.right])
            
            # update level
            level = [ leaf for node in level for leaf in (node.left,node.right) if leaf]
            # level = [leaf for leaf in next if leaf]
        ans.reverse() # 反轉list
        return ans
    # Thinking 2: 使用deque, 紀錄每次的level, 每多一個level增加一個inner list
    def levelOrderBottom2(self,root):
        queue, ans = collections.deque([(root,0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if level == len(ans): # 增加此判斷,因應level的增加而增加ans需要的list
                    ans.append([])
                ans[level].append(node.val)
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))

        return ans[::-1]

A = TreeNode(3)
B = TreeNode(9)
C = TreeNode(20)
D = TreeNode(15)
E = TreeNode(7)
A.left = B
A.right = C
C.left = D
C.right = E

Sol = Solution()
# answer = Sol.levelOrderBottom(A)
# print(answer)
answer2 = Sol.levelOrderBottom2(A)
print(answer2)
            



# You are given a binary tree in which each node contains an integer value.

# Find the number of paths that sum to a given value.

# The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

# Return 3. The paths that sum to 8 are:

# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution(object):
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: int
		"""
		if not root:
			return 0
		
		def findPath(root,sum):
			# 沒有考慮到這次不取 so 每次一進去都一定取root
			counter = 0
			if root == None:
				return 0
			if sum == root.val:
				counter += 1
			sum -= root.val
			# 找到答案後,還是有可能往下得出一樣答案
			counter += findPath(root.left,sum)
			counter += findPath(root.right,sum)
			return counter 
		# 每次return pathSum左右樹重新當root 然後放進findPath裡等回傳
		return findPath(root,sum) + self.pathSum(root.left,sum) + self.pathSum(root.right,sum)
		# return findPath(root,sum) + findPath(root.left,sum) + findPath(root.right,sum)



A = TreeNode(10)
B = TreeNode(5)
C = TreeNode(-3)
D = TreeNode(3)
E = TreeNode(2)
F = TreeNode(11)
G = TreeNode(3)
H = TreeNode(-2)
I = TreeNode(1)

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F
D.left = G
D.right = H
E.right = I

Sol = Solution()
answer = Sol.pathSum(A,8)
print(answer)
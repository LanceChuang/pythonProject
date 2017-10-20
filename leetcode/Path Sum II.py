# Given a binary tree and a sum, find all root-to-leaf paths where each 
# path's sum equals the given sum.

# For example:
# Given the below binary tree and sum = 22,
    		  # 5
        #      / \
        #     4   8
        #    /   / \
        #   11  13  4
        #  /  \    / \
        # 7    2  5   1
# return [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

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
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		output = []
		def hasPath(root,sum,path):
			if not root:
				return []
			# print(root.val)
			if not root.left and not root.right and root.val == sum:
				print(path +[root.val])
				output.append(path+[root.val])
				# return path +[root.val] # 不return就不會進去true (45行的or)
			# sum != root.val
			sum -= root.val
			# have left and right children

			# hasPath(root.left,sum,path+[root.val]) or hasPath(root.right,sum,path+[root.val])
			hasPath(root.left,sum,path+[root.val])
			hasPath(root.right,sum,path+[root.val])

			# 通常只會出現在 if else while 判斷內 或是出現在function需要return T/F的時候return
			# if root.left:
			# 	return hasPath(root.left,sum,path+[root.val])
			# elif root.right:
			# 	return hasPath(root.right,sum,path+[root.val])
		hasPath(root,sum,[])
		return output

A = TreeNode(5)
B = TreeNode(4)
C = TreeNode(8)
D = TreeNode(11)
E = TreeNode(13)
F = TreeNode(4)
G = TreeNode(7)
H = TreeNode(2)
I = TreeNode(5)
J = TreeNode(1)
A.left = B
A.right = C
B.left = D
C.left = E
C.right = F
D.left = G
D.right = H
F.left = I
F.right = J


X = TreeNode(0)
Y = TreeNode(1)
Z = TreeNode(1)
X.left = Y
X.right = Z

Sol = Solution()
# answer = Sol.pathSum(A,22)
answer = Sol.pathSum(X,1)

print(answer)
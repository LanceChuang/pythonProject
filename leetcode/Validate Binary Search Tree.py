# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def isValidBST(self,root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		# solve: inorder tree traverse
		tree_vals = []
		self.inorder(root,tree_vals)

		# compare the order and check value without same using len(set) vs len(list)

		return tree_vals == sorted(tree_vals) and len(set(tree_vals)) == len(tree_vals)
	def inorder(self,root,tree_vals):
		if root != None:
			self.inorder(root.left,tree_vals)
			tree_vals.append(root.val)
			self.inorder(root.right,tree_vals)

test = TreeNode(5)
test.left = TreeNode(3)
test.right = TreeNode(6)

ans = Solution()
print(ans.isValidBST(test))
# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

# Example 1:
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

# Sorting based solution

# For an optimized solution, begin with an example arr = [4,3,1,2]
# Sort this array. arr = [1,2,3,4]
# Now note that 1 needs to be a paired with a larger number. What is the number we would like to sacrifice? Clearly the smallest possible.
# This gives the insight: sort and pair adjacent numbers.
# Sorting takes Nlg(N) and space lg(N).

class Solution(object):
	def arrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		ans = 0
		nums.sort()
		for i in range(0,len(nums),2):
			ans += nums[i]
		return ans

test = [1,4,3,2]

answer = Solution()
ans = answer.arrayPairSum(test)
print(ans)
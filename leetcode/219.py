'''
Q:Given an array of integers and an integer k, find out whether there are two distinct 
indices i and j in the array such that nums[i] = nums[j] and the absolute difference 
between i and j is at most k.
'''

# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         dic = {}
#         for i, v in enumerate(nums):
#         	if v in dic and i - dic[v] <=k:
#         		return True
#         	dic[v] = i
#         return False


# Try = Solution()
# PPAP = Try.containsNearbyDuplicate([1,2,3,4,5,6,7,8,9,0,10,12,1,2,3],6)
# print(PPAP)
nums=[6,8,33,2,8,4,3,9,12,32,43,5]
dic = {}
k = 10
for i,j in enumerate(nums):
	if j in dic and i -dic[j] <= k:
		print("True")
	dic[j] = i

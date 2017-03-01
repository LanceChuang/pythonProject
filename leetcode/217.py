'''Given an array of integers, find if the array contains any duplicates. 
Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.'''
class Solution(object):
	def containsDuplicate(self,nums):
		if not nums:
			return False 
		PPAP = dict()
		for i in nums:
			PPAP[i] = 1 + PPAP.get(i,0)
			if PPAP[i] > 1:
				return True 
		return False
		# print(PPAP)


PPAP = Solution()
ans = PPAP.containsDuplicate([2,14,18,22,22])
print(ans)

#速解法
class Solution2(object):
	def containsDuplicate(self,nums):
		return len(nums) != len(set(nums)) # set(nums) returns distinct elements, so if repetitive,
		#the lengh of set must not the same as original length

Apple = Solution2()
ans = Apple.containsDuplicate([2,3,4,5,1])
print(ans)

nums = [1,2,3,4,5]
for i in range(len(nums)):
	print(nums[i])
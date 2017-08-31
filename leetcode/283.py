'''Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.
For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].
You must do this in-place without making a copy of the array.
Minimize the total number of operations.'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i,e in reversed(list(enumerate(nums))):
        	# print(i,e)
        	if e == 0:
        		nums.append(nums[i])
        		del nums[i]
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         book[i] = 0
        print(nums)


nums = [0, 1, 0, 3, 12]
ppap = Solution()

ppap.moveZeroes(nums)


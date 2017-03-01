'''Rotate an array of n elements to the right by k steps.'''

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        print(nums[n-k:], nums[:n-k])
        nums[:] = nums[n-k:] + nums[:n-k]
        print(nums)
nums = [1,2,3,4,5,6,7]
k = 3
ppap = Solution()
ppap.rotate(nums,k)
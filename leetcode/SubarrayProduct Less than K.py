# Your are given an array of positive integers nums.

# Count and print the number of (contiguous) subarrays where the product of all 
# the elements in the subarray is less than k.
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        
        product = 1
        count = 0
        left, right = 0,0 # sliding window pointer
        
        while right < len(nums):
            product *= nums[right]
            right += 1
            while product >= k: #and left < right :
                product /= nums[left]
                left += 1
            count += right - left
        
        return count
            
nums = [10, 5, 2, 6]
k = 100
Sol = Solution()
print(Sol.numSubarrayProductLessThanK(nums,k))
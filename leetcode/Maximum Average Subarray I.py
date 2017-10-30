# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# Note:
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 1 and k == 1:
            return nums[0] / 1.0
        # islice: elements from seq[start:stop:step]    
        maxsum = ksum = sum(itertools.islice(nums, 0, k)) # init start from 1st k elements
        
        for i in range(k,len(nums)):
            ksum += nums[i] - nums[i-k] # move forward and deduct 1 element 
            maxsum = max(maxsum,ksum)
        
        return maxsum / float(k)
        
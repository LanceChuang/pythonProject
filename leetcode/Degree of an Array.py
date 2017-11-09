# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

import collections
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        
        count = collections.Counter(nums)
        # 找element最左和最右的位置
        left,right = {}, {}
        for k,v in enumerate(nums):
            if v not in left:
                left[v] = k
            right[v] = k # 相同的element將會updated
        
        ans = len(nums) # 最大狀況就是全部都是一樣element
        degree = max(count.values())
        for i in count:
            if count[i] == degree:
                ans = min(ans, right[i] - left[i] + 1) # compare rage between left and right with ans
        
        return ans
        


import pickle
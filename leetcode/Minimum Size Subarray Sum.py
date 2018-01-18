# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not s or len(nums) == 0:
            return 0
        if sum(x for x in nums) < s : # invalid case
            return 0
        
        left, right = 0, 0
        minLength = len(nums) #+ 1
        Sum = 0
        
        while right < len(nums):
            Sum += nums[right]
            while Sum >= s:
                minLength = min(minLength, right - left + 1)
                Sum -= nums[left]
                left += 1 #左邊開始移動 
            right += 1
        return 0 if minLength > len(nums) else minLength

Sol = Solution()
print(Sol.minSubArrayLen(7,[2,3,1,2,4,3]))
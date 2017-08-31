class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # we are comparing original arr with sorted arr
        if not nums:
            return 0
        if nums == sorted(nums):
            return 0
        sorted_nums = sorted(nums)
        left = len(nums)
        right = 0
        for i in range(len(sorted_nums)):
            if sorted_nums[i] != nums[i]:
                left = min(left,i) # if index < left: left = min index
                right = max(right,i) #if index > right: right = max index
        
        if right - left >= 0:
            return right - left + 1 
      
                
            
ans = Solution()
a =ans.findUnsortedSubarray([2,6,4,8,10,9,15])
print(a)
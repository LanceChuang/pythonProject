# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements that appear twice in this array.

# Could you do it without extra space and in O(n) runtime?

# Example:
# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [2,3]
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        table = dict()
        for i in nums:
            table[i] = table.get(i,0) + 1
        return [k for k,v in table.items() if v >= 2]
        #-----正負號標記法-----#

        ans = []
        for i in range(len(nums)):
            number = abs(nums[i])
            if nums[number-1] < 0: # 出現過
                ans.append(number)
            else:
                nums[number-1] *= -1
        
        return ans            
                
Sol = Solution()
print(Sol.findDuplicates([4,3,2,7,8,2,3,1]))
# You are given two arrays (without duplicates) nums1 and nums2 where 
# nums1’s elements are subset of nums2. 
# Find all the next greater numbers for nums1's elements 
# in the corresponding places of nums2.

# The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. 
# If it does not exist, output -1 for this number.

'''
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
'''
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        great = {}
        stack = []
        
        for x in nums:
            while stack and stack[-1] < x: # means x is next greater
                element = stack.pop()
                great[element] = x
            
            stack.append(x)
        print("stack is {}".format(stack))
        for x in findNums:
            output.append(great.get(x,-1)) # if no next_Greater, then append -1
        
        return output
Solution = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
ans =Solution.nextGreaterElement(nums1,nums2)
print(ans)
'''Given a binary array, find the maximum number of consecutive 1s in this array.
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000'''

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=[]
        pointer = 0
        for i in nums:
        	if i == 0:
        		# if pointer!=0: #let pointer already sum num of 1's  
        		num.append(pointer) #temporary stored in list
        		pointer = 0
        		continue

        	if i == 1:
        		pointer += 1
        return max(num)

nums = [0,0,1,1,1,1,0,1,1,1]
ppap = Solution()
ans = ppap.findMaxConsecutiveOnes(nums)
print(ans)
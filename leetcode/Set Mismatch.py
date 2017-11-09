# The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

# Example 1:
# Input: nums = [1,2,2,4]
# Output: [2,3]
import collections
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numsWithLoss = set(nums) # remove the duplicated num 
        count = collections.Counter(nums) # keep track num of ele by Counter()
        n = len(nums)
        output = []
        # find the number occur twice
        for k,v in count.items():
            if v == 2:
                output.append(k)
        
        TrueNum = sum(range(1, n+1)) - sum(numsWithLoss)
        output.append(TrueNum)
        return output

        # another way
        out = []
        s = set()
        for x in nums:
            if x in s:
                out.append(x)
            s.add(x)
        n = len(nums)
        out.append(sum(range(1,n+1)) - sum(s))
        return out
            
        
        

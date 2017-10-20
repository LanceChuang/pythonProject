# Given an integer array nums, find the sum of the elements between 
# indices i and j (i ≤ j), inclusive.
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3

# Thinking: DP概念, 本次答案是前面答案的加總, 產生一個Sum list,第0個Sum初始為0
# 每次儲存nums該index的值以及前次的加總Sum
# SumRange(i,j) = > Sum[j+1] - Sum[i] 後面的j加總減去i前次的加總舊式範圍區間的加總
# 因為list多一個0輔助，所以輸入的 i,j => Sum[j+1]才是輸入要得index

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.Sum = [0] + nums # set first sum == 0

        # Sum[0] = 0
        for i in xrange(len(nums)):
            self.Sum[i+1] = nums[i] + self.Sum[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        answer = self.Sum[j+1] - self.Sum[i]
        return answer
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
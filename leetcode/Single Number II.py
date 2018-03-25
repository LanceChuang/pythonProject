# Given an array of integers, every element appears three times 
# except for one, which appears exactly once. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?



class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos, threes = 0, 0, 0
        for i in range(len(nums)):
            twos |= ones & nums[i] #先取出 ones 和nums[i] 中同為 1 的位元
            ones ^= nums[i] # 第一次出現的數字跟 ones 進行 XOR，把出現兩次的位元會清成 0
            threes = ones & twos # 取出 ones 跟 twos 中同為 1 的位數
            # 都是已經把出現三次的存在 three 裡了，所以把 ones 跟 twos 的清掉
            ones &= ~threes
            twos &= ~threes
        
        return ones
        
Sol = Solution()
ans = Sol.singleNumber([2,2,2,3])
print(ans)
ans = Sol.singleNumber([1,1,1,0])
print(ans)

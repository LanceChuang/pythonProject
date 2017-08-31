# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
# The algorithm should run in linear time and in O(1) space.

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        # since majority > n//3, then we have 2 counters and  the answer would be less than or equal to two numbers.
# So we can modify the algorithm to maintain two counters for two majorities.
        counter1, counter2, candidate1, candidate2 = 0,0,0,1
        
        for n in nums:
            if n == candidate1:
                counter1 += 1
            elif n == candidate2:
                counter2 += 1
            elif counter1 == 0:    # 新數字的狀況,將值給其中一個candidate
                candidate1,counter1 = n,1
            elif counter2 == 0:
                candidate2, counter2 = n,1
            else: # candidates都有數字但又出現新數字的狀況
                # print("counter1AA",counter1)
                counter1,counter2 = counter1-1, counter2-1
                print("counter1 ",counter1)
                print("counter2 ",counter2)

        
        return [n for n in (candidate1,candidate2) if nums.count(n) > len(nums)//3]

num = [1,2,1,3,3,3]
answer = Solution()
ans = answer.majorityElement(num)
print(ans)
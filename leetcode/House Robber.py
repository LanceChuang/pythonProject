# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses have security 
# system connected and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of 
# each house, determine the maximum amount of money you can rob tonight
#  without alerting the police.

# [m0,m1,m2,m3,....]，如果房子只有一間[m0]，可以偷到的錢為max = mo
# 如果有房子兩棟[m0,m1]，那最多可以拿到m0,m1之中較大的錢 max = Max(m0,m1)
# 三棟房子的情況[m0,m1,m2]，最多拿到 max = Max(m0+m2,m1);
# 因此可以得到，目前房子n，可以拿到的錢
# max = Max( 現在這棟 + 前前一可以拿到的最大金額 , 前一棟可以拿到的最大金額 )
# f(0) = nums[0]
# f(1) = max(num[0], num[1])
# f(k) = max( f(k-2) + nums[k], f(k-1) )
class Solution(object):
	def rob(self,nums):
		last, now = 0, 0

		for i in nums: 
			last, now = now, max(last + i, now)

		return now

	# O(n) space寫法
	def rob2(self,nums):
		if len(nums) == 0:
			return 0
		if len(nums) == 1:
			return nums[0]
		if len(nums) == 2:
			return max(nums[0],nums[1])

		maxProfit = []
		maxProfit.append(nums[0]) # 1st as default max
		maxProfit.append(max(nums[0],nums[1]))

		for i in range(2,len(nums)):
			# 最大金額   = Max(現在金額+前前一棟最大金額 ， 前一棟最大金額)
			maxProfit.append(max(nums[i]+maxProfit[i-2],maxProfit[i-1]))

		return maxProfit.pop()


target = [2,4,5,3,1]
Sol = Solution()
answer = Sol.rob2(target)
print(answer)
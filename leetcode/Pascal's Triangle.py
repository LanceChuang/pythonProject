'''Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
	def generate(self,numRows):
		"""
        :type numRows: int
        :rtype: List[List[int]]
		"""
		ans = []
		# decide how many sub-list we need
		for i in range(numRows):
			ans.append([1]*(i+1))
		# print(ans)
			if i >1:
				for j in range(1,i):
					ans[i][j] = ans[i-1][j-1] + ans[i-1][j] #　add from previous level
		# print(ans)
		return ans

answer = Solution()
ans = answer.generate(5)
print(ans)
# Given n, how many structurally unique BST's (binary search trees) 
# that store values 1...n?

# For example,
# Given n = 3, there are a total of 5 unique BST's.
  #  1         3     3      2      1
  #   \       /     /      / \      \
  #    3     2     1      1   3      2
  #   /     /       \                 \
  #  2     1         2                 3

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0 :
            return 0
        
        root = [0] * (n+1)
        return self.count(n,root)
    
    def count(self,n,root):
        # base case
        if n == 0 or n == 1:
            return 1
        
        if root[n] != 0: # 檢查有無已經有的答案
            return root[n]
        
        Sum = 0
        for i in range(n):
            Sum += self.count(i,root) * self.count(n-i-1,root)
        
        root[n] = Sum 
        
        return Sum
    
    # 使用DP解
    def numTrees1(self,n):
    	if n <= 0 :
    		return 0 
    	count = [0] * (n+1)
    	count[0] = 1

    	for i in range(1,n+1):
    		for j in range(i):
    			count[i] += count[j] * count[i-j-1]
    			print("count[i]",count[i])
    			print("count[j]",count[j])
    			print("count[i-j-1]",count[i-j-1])

    	return count[n]


target = 3
Sol = Solution()
answer = Sol.numTrees(target)
print(answer)
answer2 = Sol.numTrees1(target)
print(answer2)
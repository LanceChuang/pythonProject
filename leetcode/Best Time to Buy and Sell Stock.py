# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction 
# (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5

# max. difference = 6-1 = 5 
# (not 7-1 = 6, as selling price needs to be larger than buying price)
# Input: [7, 6, 4, 3, 1]
# Output: 0

# In this case, no transaction is done, i.e. max profit = 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        temp = 0
        res = 0
        # find maximum price and then the big difference
        for i in range(len(prices)-1,-1,-1):
            temp = max(prices[i],temp)
            if temp - prices[i] > res:
                res = temp - prices[i]
        
        # another way - find  largest peak following the smallest valley.
        minprice = 10000000000000000
        maxprofit = 0
        for i in range(len(prices)):
        	if prices[i] < minprice:
        		minprice = prices[i]
        	elif prices[i] - minprice > maxprofit:
        		maxprofit = prices[i] - minprice
        # return maxprofit 

        return res
stockP = [7,1,5,3,6,4]
Sol = Solution()
print(Sol.maxProfit(stockP))
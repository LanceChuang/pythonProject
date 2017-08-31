# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


# Assume we buy a stock yesterday, what will we do today?

# If today's price is higher than yesterday, we can sell it right now and get profit.
# What's about tomorrow the price grows higher?We just buy today's stock, that's equal to that we buy yesterday and sell tomorrow.
# What if today's price is lower than yesterday's? We just pretend we buy today's stock but not yesterday's .
# In a word, what's we should do is compare today's price to yesterday's.If higher,we get profit,
# set buy-in price to today's price.If lower, we don't get profit,and set buy-in price to today's price.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 今天價格比昨天高 = 買今天,賣昨天
        # 今天價格比昨天低 = 今天價格為新的買入價
        if len(prices) < 2:
            return 0
    
        buyIn = prices[0] # 0 as default day
        res = 0 
        for i in range(1,len(prices)):
            profit = prices[i] - buyIn
            if profit > 0:
                res += profit
            buyIn = prices[i]
        
        return res 
prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))

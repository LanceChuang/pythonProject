# Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
# However, flowers cannot be planted in adjacent plots - 
# they would compete for water and both would die.

# Given a flowerbed (represented as an array containing 0 and 1, 
# where 0 means empty and 1 means not empty), and a number n, 
# return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False

'''
思考:
給一個counter算出最多能種植幾個空位
loop over the flowerbed,看左右是否為0
沒有的話填上1佔領該空位
最左邊不用檢查左邊 , 最右邊不用檢查右邊
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = 0
        count = 0 # count extra maximum number of flowers
        while i < len(flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1 # 佔領該格
                count += 1
            i += 1
        
        return count >= n
Sol =  Solution()
print(Sol.canPlaceFlowers([1,0,0,0,1],1))
print(Sol.canPlaceFlowers([1,0,0,0,0,0,1],2))
        
# You are playing the following Nim Game with your friend: 
# There is a heap of stones on the table, each time one of you 
# take turns to remove 1 to 3 stones. 
# The one who removes the last stone will be the winner. 
# You will take the first turn to remove the stones.

# Both of you are very clever and have optimal strategies for the game. 
# Write a function to determine whether you can win the game 
# given the number of stones in the heap.

# For example, if there are 4 stones in the heap, 
# then you will never win the game: no matter 1, 2, or 3 stones you remove,
#  the last stone will always be removed by your friend.

# Thinking:
# 石頭數量小於等於3，直接獲勝
# 石頭數量等於4個，輸
# 石頭數量5個，先拿走1個，獲勝
# 由以上可以推論(5-1=4, 6-2=4, 7-3=4) 5~7都可以獲勝
# 石頭數量8個，不管怎樣都會輸
# 以上可以得到結論，只要一開始的石頭數量為4的倍數，就會輸。
class Solution(object):
	def canWinNim(self,n):
		"""
		:type n: int
		:rtype: bool
		"""
		# if n < 4:
		# 	return True
		# if n % 4 == 0:
		# 	return False
		# else:
		# 	return True
		return n % 4 != 0 

Sol = Solution()
answer = Sol.canWinNim(5)
print(answer)


# Determine whether an integer is a palindrome. Do this without extra space.
# Could negative integers be palindromes? (ie, -1)

# If you are thinking of converting the integer to string, note the restriction of using extra space.

# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

# There is a more generic way of solving this problem

# Thinking: 
# 計算一個數字是否是回文數字，將這個數字除以10，保留他的餘數，
# 下次將餘數乘以10，加上這個數字再除以10的餘數.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #負數不是Palindrome
        if x < 0 :
            return False
        elif x == 0: # 0 is Palindrome
            return True

        left = 0 #餘數
        origin = x
        while x != 0:
            left = left * 10 +x % 10
            x = x // 10 # 往左推進
        # print("left",left)
        return left == origin

Sol = Solution()
ans = Sol.isPalindrome(121)
print(ans)
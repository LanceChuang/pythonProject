# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

# For example:

# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
#         if num < 10:
#             return num
        
#         while num >= 10:
#             first = num % 10
#             rest = num / 10
#             num = first + rest
        
#         return num
        
        
        # Math Theorem solution
        if num < 10:
            return num
        
        if num % 9 == 0:
            return 9
        
        return num % 9
        
            
            
Answer = Solution()
ans = Answer.addDigits(36)
print(ans)
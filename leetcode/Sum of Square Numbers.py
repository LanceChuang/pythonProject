# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False

# Thinking : Binary Search , c - a*2 = b*b
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0 :
            return False
        
        left = 0
        right = int(math.sqrt(c))
        # print right
        
        while left <= right:
            currentAnswer = left*left + right*right
            if currentAnswer == c:
                return True
            elif currentAnswer > c:
                right -= 1
            elif currentAnswer < c:
                left += 1
        
        return False # no match
        
        
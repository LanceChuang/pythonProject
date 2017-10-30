# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example:
# Given num = 16, return true. Given num = 5, return false.

# Follow up: Could you solve it without loops/recursion?

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # bit manipulation
        
        # 2 criteria for a number to be power of 4:
        # is power of 2: n&(n-1) == 0
        # even number of "0" in binary format
        #"{0:b}".format  => binary format of 0
        
        # print(len("{0:b}".format(num)))
        return num > 0 and num & (num-1) == 0 and len("{0:b}".format(num)) % 2 == 1 

answer = Solution()
ans = answer.isPowerOfFour(4)
print(ans)
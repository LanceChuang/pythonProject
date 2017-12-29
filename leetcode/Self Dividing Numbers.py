# Self Dividing Numbers
# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

# Also, a self-dividing number is not allowed to contain the digit zero.

# Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

# Example 1:
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_dividable(num):
            s = str(num)
            for x in s:
                if x == "0" or num % int(x) != 0:
                    return False
            return True
        
        res = []
        for i in range(left,right+1):
            if i != 0 and i <= 9:
                res.append(i)
            elif i % 10 == 0: # contains 0
                continue
            else:
                if is_dividable(i):
                    res.append(i)
        print(res)
        return res
        # return [i for i in result]
                
            
Sol = Solution()
print(Sol.selfDividingNumbers(1,22))                

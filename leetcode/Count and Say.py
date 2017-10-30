# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        res = "1"
        for i in range(n-1): # first is "1"
            first, temp, count = res[0], "", 0 # init first letter each loop, temp to store
            for x in res:
                if x == first:
                    count += 1
                else: # meet different letter, store past answers
                    temp += str(count) + first
                    first = x # different letter becomes first letter
                    count = 1
            temp += str(count) + first
            res = temp # update the answer string 
        return res
                    
        
        
# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.

# check out rule : Subtractive notation

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        result = 0
        prev = 0
        
        for i in range(len(s)-1,-1,-1):
            current = hash[s[i]]
            # 後面比前面大就要subtraction前面的值
            if current < prev:
                result -= current
            else:
                result += current
            
            prev = current
        
        return result

target = "CCXLVI"                
Sol = Solution()
ans = Sol.romanToInt(target)
print(ans)


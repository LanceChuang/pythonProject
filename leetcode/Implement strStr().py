# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) == 0 and len(needle) == 0:
            return 0
        
        if needle not in haystack:
            return -1
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle: # 檢查每次slice往後needle大小的str是否等於needle去慢慢逼近答案
                return i
        return -1
   
haystack = "hello"
needle = "ll"        
Sol = Solution()
print(Sol.strStr(haystack,needle))
haystack = "aaaaa"
needle = "bba"   
print(Sol.strStr(haystack,needle))

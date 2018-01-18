# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

# This is case sensitive, for example "Aa" is not considered a palindrome here.

# Note:
# Assume the length of given string will not exceed 1,010.

# Example:

# Input:
# "abccccdd"

# Output:
# 7

# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = collections.Counter(s)
        print counter
        odd = 0
        for k,v in counter.items(): 
            odd += v % 2 # 找尋奇數的個數,去除單一的奇數,最多只用一個剩餘奇數
        
        return len(s) - odd + 1 if odd > 0 else len(s)
# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Given s = "hello", return "holle".

# Example 2:
# Given s = "leetcode", return "leotcede".
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowel = set(list('aeiouAEIOU'))
        left, right = 0, len(s) - 1
        
        while left < right:
            while s[left] not in vowel and left < right:
                left += 1
            while s[right] not in vowel and left < right:
                right -= 1
            # meet vowels
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
        
        return "".join(s)
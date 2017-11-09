# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) == len(t) and s[:] == t[:]:
            return s[:]
        counter = collections.Counter(t)
        missing = len(t)
        min_length = 1000000
        min_start = 0
        start = end = 0 # default from 0
        
        while end < len(s):
            if counter[s[end]] > 0: # match the s and t
                missing -= 1
            # current window contains s[end] now , does not need it anymore
            counter[s[end]] -= 1
            end += 1 # move right
            while missing == 0: # when nothing missing => move start to right
                if min_length > end - start:
                    min_length = end - start
                    min_start = start
                # current window does not contain s[start] so need to add 1 since we lost it
                counter[s[start]] += 1
                if counter[s[start]] > 0:
                    missing += 1
                start += 1 # move start pointer
        
        return "" if min_length == 1000000 else s[min_start:min_start+min_length]
                
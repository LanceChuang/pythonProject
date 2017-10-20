# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

# For example,
# Given "egg", "add", return true.

# Given "foo", "bar", return false.

# Given "paper", "title", return true.

# Note:
# You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_length = len(s)
        t_length = len(t)
        if s_length != t_length:
            return False
        
        data1, data2 = {}, {}
        # 以val為index, key為value, 找出原位置的差異
        for key,val in enumerate(s):
            data1[val] = data1.get(val,[]) + [key] # if have val, append its index to value
        for key,val in enumerate(t):
            data2[val] = data2.get(val,[]) + [key]
            
        return sorted(data1.values()) == sorted(data2.values())

s = "egg"
g = "app"
Sol = Solution()
answer = Sol.isIsomorphic(s,g)
print(answer)




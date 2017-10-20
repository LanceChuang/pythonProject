# A message containing letters 
# from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given an encoded message containing digits, determine the total number of
#  ways to decode it.

# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

# The number of ways decoding "12" is 2.

# Thinking:
# f(n) = f(n-1)(s[n]!=0)
# 	   + f(n-2)(s[n-1]與s[n]組成在10-26)
# 0不對應任何字

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        f = [0] *(len(s)+1)
        f[0] = 1
        
        for i in range(1,len(s)+1):
            
            if s[i-1] != '0':
                f[i] += f[i-1]
                print("f[i-1]",f[i-1])
            
            if i >= 2 and s[i-2:i] < "27" and s[i-2:i] > "09": # "01" ways = 0
                f[i] += f[i-2]
                print("f[i-2]",f[i-2])
                # print("i=",i) # 2 
        # print(f) # [1,1,2]
        
        return f.pop()
                
target = "7452310519"
target = "24"
Sol = Solution()
answer = Sol.numDecodings(target)
print(answer)

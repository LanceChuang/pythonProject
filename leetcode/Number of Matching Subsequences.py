import collections

class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """


        # scan words and check in word_dict
        num = 0 # init num of sub
        for word in words:
        	index = 0
        	flag = 0
        	for char in word:
        		index = S.find(char, index) # inside index means begins from 
        		if index == -1: # did not find it
        			flag = 1
        			break
        		index += 1
        	if flag == 0 : # flag == 0 means match
        		num += 1
        		
        return num




words = ['a', 'bb', 'acd', 'ace']
S = "abcde"
Sol = Solution()
ans = Sol.numMatchingSubseq(S, words)
print(ans)
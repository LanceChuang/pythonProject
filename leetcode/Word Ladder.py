# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# For example,

# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        queue = collections.deque()
        wordList = set(wordList)
        queue.append([beginWord,1])
        
        
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step
            
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nextWord = word[:i] + c + word[i+1:] # try every possible combination
                    if nextWord in wordList:
                        wordList.remove(nextWord)
                        queue.append([nextWord,step+1])
        
        return 0
        
Solutions = Solution()
ans = Solutions.ladderLength("hit", "cog",["hot","dot","dog","lot","log","cog"])
print(ans)
# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper() or word == word.lower():
            return True
        for letter in range(1,len(word)):
            if word[letter] == word[letter].upper():
                return False
        return True
        
        # another way
        # isupper() - check all chars in upper
        # istitle() - check first letter is upper and others are lower
        return word.isupper() or word.islower() or word.istitle()

sol = Solution()
ans = sol.detectCapitalUse("UsA")
print(ans)
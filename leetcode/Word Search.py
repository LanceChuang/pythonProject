# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.
# For example,
# Given board =

# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == []:
        	return False 
        if len(board) == 0:
        	return False

        for row in range(len(board)):
        	for col in range(len(board[0])):
        		if board[row][col] == word[0]:
        			if self.dfs(board,word,row,col):
        				return True 
        return False 

    def dfs(self,board,word,row,col):
        # find the first match in board for word first letter
        if board[row][col] == word[0]:
            if not word[1:]: # if not adjacents
                return True

            board[row][col] = " " # used cell symbol
            # up 
            if row > 0 and self.dfs(board,word[1:],row-1,col):
            	return True
            # down
            if row < len(board) - 1 and self.dfs(board,word[1:],row+1,col):
            	return True 
            # left
            if col > 0 and self.dfs(board,word[1:],row,col-1):
            	return True 
            # right
            if col < len(board[0]) - 1 and self.dfs(board,word[1:],row,col+1):
            	return True 

            board[row][col] = word[0] # updated to its original
            return False 
        else:
        	return False 


if __name__ == "__main__":
	board = [
			  ['A','B','C','E'],
			  ['S','F','C','S'],
			  ['A','D','E','E']
			]
	word = "ABCCED"
	Sol = Solution()
	ans = Sol.exist(board,word)
	print(ans)
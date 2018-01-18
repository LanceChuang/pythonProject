# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n : return []
        # init - matrix
        ans = []
        for i in range(n):
            tmp = []
            for j in range(n):
                tmp.append(0)
            ans.append(tmp)
        
        # init - attr
        left = 0
        right = n-1
        top = 0
        bottom = n-1
        num = 1 # 要填入的數字
        
        while left <= right:
            # left -> right 
            for i in range(left, right+1):
                ans[top][i] = num
                num += 1
            top += 1
            # top -> bottom
            for i in range(top,bottom+1):
                ans[i][right] = num
                num += 1
            right -= 1
            # right -> left
            for i in range(right,left-1,-1):
                ans[bottom][i] = num
                num += 1
            bottom -= 1
            # bottom -> top
            for i in range(bottom, top-1,-1):
                ans[i][left] = num
                num += 1
            left += 1
        
        return ans
        
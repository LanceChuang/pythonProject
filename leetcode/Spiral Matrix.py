# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        n = len(matrix[0])
        m = len(matrix)
        left = 0
        right = n-1
        top = 0
        bottom = m-1
        ans = []
        while left < right and top < bottom:
            ans.extend([ matrix[top][i] for i in range(left,right)]) # 右邊少跑一個
            ans.extend([ matrix[i][right] for i in range(top,bottom)]) # 下面少跑一個
            ans.extend([ matrix[bottom][i] for i in range(right,left,-1)]) # 左邊少跑一個
            ans.extend([ matrix[i][left] for i in range(bottom,top,-1)]) # 上面少跑一個
            
            left +=1
            right -= 1
            top += 1
            bottom -= 1
        # special case - 最後一圈沒有上下左右邊
        # OOOOO
        # OXXXO
        # OOOOO       
        if left == right:
            ans.extend([ matrix[i][right] for i in range(top,bottom+1)])
        elif top == bottom:
            ans.extend([ matrix[top][i] for i in range(left,right+1)])
        return ans
        
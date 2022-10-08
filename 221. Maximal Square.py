"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

ref: https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

"""

# DP approach
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]
        m = len(matrix)
        n= len(matrix[0])
        ans = 0
        
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if i == m-1 and j==n-1:
                    dp[i][j] = int(matrix[i][j])
                
                elif i == m-1:
                    dp[i][j] = int(matrix[i][j])
                
                elif j ==n-1:
                    dp[i][j] = int(matrix[i][j])
                
                else:
                    if matrix[i][j]=='0':
                        dp[i][j] = int(matrix[i][j])
                    else:
                        mn = min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])
                        dp[i][j]=mn+1
                
                if dp[i][j]>ans:
                        ans = dp[i][j]
        return ans**2
        
# Using Stack ..........................................................

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m  = len(matrix)
        n = len(matrix[0])
        maxHeight = []
        for i in range(m):
            maxHeight.append([0]*n)
        for j in range(n):
            maxH = 0
            for i in range(m-1,-1,-1):
                if matrix[i][j] == "1":
                    maxH += 1
                else:
                    maxH = 0
                maxHeight[i][j] = maxH
        def maxArea(row):
            stack = [(0, row[0])]
            mA = 0
            lr = len(row)
            for i in range(1,lr):
                hi = row[i]
                while stack and stack[-1][1] > hi:
                    ind, height = stack.pop()
                    leftBound = stack[-1][0]+1 if stack else 0
                    rightBound = i
                    
                    areai = min(rightBound - leftBound, height) ** 2
                    if areai > mA:
                        mA = areai
                stack.append((i, hi))
            rightBound = lr
            while stack:
                ind, height = stack.pop()
                leftBound = stack[-1][0]+1 if stack else 0
                areai = min(rightBound - leftBound, height) ** 2
                if areai > mA:
                    mA = areai
            return mA
        maxA = 0
        for row in range(m):
            maxRowArea = maxArea(maxHeight[row])
            if maxRowArea > maxA:
                maxA = maxRowArea
        return maxA




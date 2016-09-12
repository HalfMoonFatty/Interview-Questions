'''
Problem:

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution:

    def minPathSum(self, grid):

        m,n = len(grid), len(grid[0])
        dp = [[sys.maxint] * (n+1) for _ in range(m+1)]    # note init as maxint
        
        dp[1][1] = grid[0][0]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if not (i == 1 and j == 1): # note
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i-1][j-1]
                
        return dp[-1][-1]





class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m,n = len(grid),len(grid[0])

        # init values for corner dp[0][0] and edges dp[0][c] and dp[r][0]
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        return dp[m-1][n-1]
